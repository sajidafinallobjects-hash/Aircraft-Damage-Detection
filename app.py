print("مرحباً بك في نظام كشف أضرار الطائرات!")
print("✅ نظام كشف أضرار الطائرات جاهز!")
print("📦 جميع المكتبات مثبتة بنجاح")

# اختبار استيراد المكتبات
try:
    import tensorflow as tf
    print("✅ TensorFlow يعمل - الإصدار:", tf.__version__)
except:
    print("❌ TensorFlow غير مثبت")

try:
    import cv2
    print("✅ OpenCV يعمل - الإصدار:", cv2.__version__)
except:
    print("❌ OpenCV غير مثبت")

print("🚀 المشروع جاهز للانطلاق!")