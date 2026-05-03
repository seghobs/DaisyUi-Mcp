# DaisyUI Expert Python MCP Server 🚀

Bu Python tabanlı MCP sunucusu, 65+ DaisyUI bileşeninin tüm dökümantasyonunu içeren `component_content.md` dosyasını (5.3MB) bir bilgi bankası olarak kullanır. Cursor, Antigravity ve Claude Code gibi yapay zeka araçlarıyla tam uyumludur.

## 🛠️ Kurulum

### 1. Gereksinimler
Python 3.10+ ve `mcp` kütüphanesi gereklidir.
```bash
pip install mcp
```

### 2. IDE Entegrasyonu ve .json Yapılandırması

MCP sunucusunu kullanmak için IDE'nizin (Cursor, Claude Desktop vb.) yapılandırma dosyasına (`mcp_config.json`) aşağıdaki bloğu eklemeniz gerekir.

#### 📝 mcp_config.json Örneği

```json
{
  "mcpServers": {
    "daisyui-expert": {
      "command": "python",
      "args": [
        "c:/Users/user/Desktop/Daisyui-mcp/daisyui_mcp.py"
      ],
      "env": {}
    }
  }
}
```

> [!TIP]
> **Dosya Yolu:** Yukarıdaki `"args"` kısmındaki `c:/Users/user/Desktop/Daisyui-mcp/daisyui_mcp.py` yolunun, dosyanın bilgisayarınızdaki gerçek yolu olduğundan emin olun. Ters eğik çizgi (`\`) yerine düz eğik çizgi (`/`) kullanmak Windows üzerinde daha güvenlidir.

---

## 🔍 Kullanılabilir Araçlar (Tools)

1. **`list_components`**: Kütüphanedeki tüm bileşenlerin listesini verir (65+ bileşen).
2. **`get_component(name)`**: Belirli bir bileşenin tüm kod örneklerini, HTML yapılarını ve DaisyUI v5 varyasyonlarını getirir.
   - Örn: `get_component("button")` veya `get_component("modal")`
3. **`search_docs(query)`**: Tüm dökümantasyon içinde anahtar kelime araması yapar.
   - Örn: `search_docs("dark mode support")`
4. **`expert_instruction` (Prompt)**: AI'ya "DaisyUI Uzmanı" gibi davranmasını ve her 'daisyui' dendiğinde otomatik olarak bu MCP'yi kullanmasını söyler.

---

## 🚀 Proaktif Tetikleme (Proactive Trigger)

Artık sunucumuzda özel bir kural tanımlı: **'daisyui', 'daisy ui' veya 'daisy mcp'** kelimelerini kullandığınızda, AI otomatik olarak:
- Bileşen listesini kontrol eder.
- İlgili bileşenin dökümantasyonunu getirir.
- Tasarım önerilerini otomatik olarak uygular.

Bu özelliği aktif etmek için AI modelinize şu talimatı vermeniz yeterlidir: *"DaisyUI MCP promptunu kullan."*

---

## ✨ Neden Bu Sunucu?

- **Veri Odaklı**: LLM'ler (Yapay Zeka modelleri) DaisyUI sınıflarını uydurmak (hallucination) yerine doğrudan `component_content.md` dosyasındaki gerçek verilere bakar.
- **Antigravity Optimized**: Her sorgu yanıtına otomatik olarak premium tasarım ipuçları ve modern CSS pratikleri eklenir.
- **Python Hızı**: 5.3MB'lık veriyi anında tarayabilen optimize edilmiş bir arama motoru gibi çalışır.
- **Temiz Kod**: Sadece `daisyui_mcp.py` dosyasını çalıştırarak tüm DaisyUI evrenini AI'nızın emrine verirsiniz.

---

## 📂 Dosya Yapısı
- `daisyui_mcp.py`: Sunucu mantığı ve araç tanımları.
- `component_content.md`: DaisyUI v5.x ana bilgi kaynağı.
- `merge.ps1`: (Opsiyonel) Dökümanları güncellemek için kullanılan script.

---
**Tasarım Notu:** Bu sunucu, AI'nın "premium" tasarımlar üretmesini zorunlu kılan bir tasarım felsefesiyle (Design Philosophy) donatılmıştır.
