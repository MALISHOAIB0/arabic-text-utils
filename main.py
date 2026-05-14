# main.py
def count_words(text):
    """عدد الكلمات في النص (افترض أن المسافات تفصل بينها)"""
    if not text:
        return 0
    return len(text.split())

def count_characters(text):
    """عدد الحروف (بما فيها المسافات)"""
    return len(text)

def is_arabic(text):
    """التحقق إذا كان النص يتكون من أحرف عربية (بسيط)"""
    arabic_unicode_range = range(0x0600, 0x06FF)
    for ch in text:
        if ord(ch) in arabic_unicode_range:
            return True
    return False

# مثال بسيط للاختبار إذا تم تشغيل الملف مباشرة
if __name__ == "__main__":
    sample = "مرحبا بالعالم"
    print(f"النص: {sample}")
    print(f"عدد الكلمات: {count_words(sample)}")
    print(f"عدد الحروف: {count_characters(sample)}")
    print(f"هل هو عربي؟ {is_arabic(sample)}")
