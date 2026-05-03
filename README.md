# DaisyUI MCP Server (Python)

Bu sunucu, DaisyUI v5 ve Tailwind CSS v4 kullanarak yüksek kaliteli, modern ve premium UI bileşenleri oluşturmanıza yardımcı olan bir Model Context Protocol (MCP) sunucusudur.

## 🚀 Özellikler
- **65+ Bileşen**: DaisyUI kütüphanesindeki tüm bileşenlerin kod örnekleri ve dökümantasyonu.
- **Hızlı Arama**: `search_docs` ile ihtiyacınız olan özelliği anında bulun.
- **Hazır Şablon**: `get_boilerplate` ile saniyeler içinde yeni bir projeye başlayın.
- **Proaktif Tasarım**: AI'nın DaisyUI uzmanı gibi davranmasını sağlayan özel promptlar.

## 🛠️ Kurulum

### 1. Python Gereksinimi
Python 3.10 veya daha yeni bir sürümün yüklü olduğundan emin olun.

### 2. Kütüphanelerin Yüklenmesi
Terminalinizde aşağıdaki komutu çalıştırarak gerekli MCP kütüphanesini yükleyin:
```bash
pip install mcp
```

### 3. IDE Konfigürasyonu (Cursor / Claude Desktop / Antigravity)
Aşağıdaki JSON içeriğini IDE'nizin MCP ayarları kısmına (`mcp_config.json`) ekleyin.

> [!IMPORTANT]
> `command` kısmındaki dosya yolunu, bu klasörü bilgisayarınızda nereye indirdiyseniz oraya göre güncellemeyi unutmayın!

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

## 🔍 Kullanılabilir Araçlar (Tools)

- `list_components`: Tüm bileşenleri listeler.
- `get_component(name)`: Belirli bir bileşenin HTML/CSS kodlarını getirir.
- `search_docs(query)`: Dökümantasyon içinde arama yapar.
- `get_boilerplate`: DaisyUI v5 + Tailwind v4 başlangıç kodunu verir.

## 📄 Lisans
MIT
