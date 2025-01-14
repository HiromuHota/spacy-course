def test():
    assert (
        "import Doc, Span" or "import Span, Doc" in __solution__
    ), "DocとSpanをきちんとインポートしましたか？"
    assert doc.text == "I like David Bowie", "docをきちんと作成しましたか？"
    assert span.text == "David Bowie", "spanをきちんと作成しましたか？"
    assert span.label_ == "PERSON", "spanにPERSONラベルを追加しましたか？"
    assert "doc.ents =" in __solution__, "doc.entsを上書きしましたか？"
    assert len(doc.ents) == 1, "doc.entsにスパンを追加しましたか？"
    assert list(doc.ents)[0].text == "David Bowie", "doc.entsにスパンを追加しましたか？"
    __msg__.good(
        "完璧です！spaCyのオブジェクトを手動で作成し、固有表現を更新しました。" "これは後ほど、カスタムパイプラインコンポーネントを作成する際に役に立ちます。"
    )
