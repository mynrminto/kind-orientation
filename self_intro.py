"""オリエンテーション課題: Codex と一緒に作った自己紹介スクリプト。"""

PROFILE = {
    "名前": "サンプル太郎",
    "所属": "KInd Agents(医学生)",
    "興味": "臨床データの機械学習",
    "今後学びたいこと": "ロジスティック回帰から画像診断AIまで",
}


def main():
    print("=" * 30)
    for key, value in PROFILE.items():
        print(f"{key}: {value}")
    print("=" * 30)


if __name__ == "__main__":
    main()
