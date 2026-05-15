import sys

def classify_support_ticket(message: str) -> dict:
    """
    Simulates an AI model classifying a customer support ticket.
    In a real-world scenario, this would involve a deployed machine learning model
    (e.g., a text classifier) performing inference.

    For this example, we use simple keyword matching to demonstrate the concept.
    """
    message_lower = message.lower()
    
    category = "General Inquiry"
    priority = "Medium"
    suggested_action = "Forward to general support queue."

    # Simulate AI classification logic based on keywords (e.g., a simple text classifier)
    if any(keyword in message_lower for keyword in ["hata", "çalışmıyor", "problem", "kurulum", "bağlantı", "teknik"]):
        category = "Technical Support"
        suggested_action = "Route to Technical Support Team. Provide troubleshooting guide."
        if any(keyword in message_lower for keyword in ["acil", "kritik", "hemen"]):
            priority = "High"
    elif any(keyword in message_lower for keyword in ["fatura", "ödeme", "ücret", "abonelik", "iptal", "para"]):
        category = "Billing"
        suggested_action = "Route to Billing Department. Check customer's account history."
    elif any(keyword in message_lower for keyword in ["ürün", "fiyat", "satın alma", "bilgi", "kampanya"]):
        category = "Sales/Product Inquiry"
        suggested_action = "Route to Sales Team. Offer product catalog or demo."
    elif any(keyword in message_lower for keyword in ["geri bildirim", "öneri", "şikayet"]):
        category = "Feedback/Complaint"
        suggested_action = "Route to Customer Experience Team. Log feedback."

    return {
        "original_message": message,
        "category": category,
        "priority": priority,
        "suggested_action": suggested_action
    }

def main():
    print("Maliyet Odaklı AI Destek Triage API Simülasyonu")
    print("------------------------------------------------")
    print("Müşteri destek mesajını girin (çıkmak için 'q' yazın):")

    while True:
        try:
            user_input = input("> ")
            if user_input.lower() == 'q':
                break
            if not user_input.strip():
                print("Lütfen geçerli bir mesaj girin.")
                continue

            # In a real serverless inference setup, this message would be sent to an API Gateway
            # which triggers a serverless function (e.g., DigitalOcean Functions, AWS Lambda).
            # That function would then load and execute the AI model (like classify_support_ticket).
            # This 'pay-per-execution' model is key to cost-effective AI inference.
            print("\nAI Triage sistemi mesajı işliyor...")
            triage_result = classify_support_ticket(user_input)
            
            print("\n--- Triage Sonuçları ---")
            print(f"Orijinal Mesaj: {triage_result['original_message']}")
            print(f"Kategori: {triage_result['category']}")
            print(f"Öncelik: {triage_result['priority']}")
            print(f"Önerilen Eylem: {triage_result['suggested_action']}")
            print("------------------------")
            print("\n")

        except EOFError: # Handle Ctrl+D
            break
        except Exception as e:
            print(f"Bir hata oluştu: {e}")
            break

    print("Simülasyon sona erdi. Hoşça kalın!")

if __name__ == "__main__":
    main()
