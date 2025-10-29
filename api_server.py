# 顶部导入区域
import json
import uuid
import time
from typing import Dict, Any, Generator

from flask import Flask, request, jsonify, Response, stream_with_context, send_file
import os

app = Flask(__name__)

# 简易内存任务表（占位）
TASKS: Dict[str, Dict[str, Any]] = {}


def sse_event(event_name: str, data: Dict[str, Any]) -> str:
    """格式化 SSE 事件"""
    return f"event: {event_name}\n" + f"data: {json.dumps(data, ensure_ascii=False)}\n\n"


@app.route("/api/tasks", methods=["POST"])
def create_task():
    """创建任务（不实现具体业务，仅返回 taskId）"""
    try:
        payload = request.get_json(force=True, silent=False) or {}
    except Exception:
        return jsonify({"error": "invalid request body"}), 400

    task_text = (payload.get("task") or "").strip()
    if not task_text:
        return jsonify({"error": "task is required"}), 400

    task_id = str(uuid.uuid4())
    TASKS[task_id] = {
        "id": task_id,
        "task": task_text,
        "status": "created",
        "created_at": int(time.time()),
        # 可在此扩展：agents 队列、上下文、用户信息等
    }
    return jsonify({"taskId": task_id}), 200


@app.route("/", methods=["GET"])
def index():
    return send_file(os.path.join(os.path.dirname(__file__), "front.html"))


@app.route("/api/tasks/<task_id>/stream", methods=["GET"])
def stream_task(task_id: str):
    """任务 SSE 流（占位实现，不推送真实智能体数据）"""
    if task_id not in TASKS:
        return jsonify({"error": "task not found"}), 404

    @stream_with_context
    def generate() -> Generator[str, None, None]:
        # 连接建立提示
        yield sse_event("progress", {"message": "SSE已连接，等待智能体输出..."})
        time.sleep(0.5)

        # 占位事件：任务解析智能体
        yield sse_event("taskAgent", {"status": "running", "result": "任务解析中..."})
        time.sleep(0.8)
        yield sse_event("taskAgent", {"status": "completed", "result": "任务解析完成"})

        # 占位事件：搜索智能体
        yield sse_event("searchAgent", {"status": "running", "result": "搜索进行中..."})
        time.sleep(0.8)
        yield sse_event("searchAgent", {"status": "completed", "result": "找到5条数据"})

        # 占位事件：制图智能体（使用占位图）
        yield sse_event("chartAgent", {
            "status": "completed",
            "result": "图表就绪",
            "imageUrl": "https://dummyimage.com/800x400/3498db/ffffff.png&text=Stock+Chart"
        })
        time.sleep(0.5)

        # 占位事件：评论智能体（最后一个，输出完整评论）
        yield sse_event("commentAgent", {
            "status": "completed",
            "fullComment": "综合评论（示例）：趋势平稳，建议谨慎观察。"
        })

        # 收尾事件
        yield sse_event("done", {"message": "所有智能体已完成（占位示例）"})

    headers = {
        "Content-Type": "text/event-stream",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        # 反向代理时建议关闭缓冲
        "X-Accel-Buffering": "no",
    }
    return Response(generate(), headers=headers)


if __name__ == "__main__":
    # 可根据需要调整 host/port/debug
    app.run(host="127.0.0.1", port=5000, debug=True)