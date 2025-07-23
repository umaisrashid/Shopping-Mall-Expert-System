from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

product_database = {
   "electronics": [
    {
        "name": "Premium Wireless Headphones",
        "category": "Electronics",
        "price": 199.99,
        "rating": 5,
        "reviews": 1243,
        "description": "Noise-cancelling wireless headphones with 30-hour battery life and premium sound quality.",
        "features": ["Bluetooth 5.0", "Active Noise Cancellation", "30hr battery"],
        "keywords": ["headphones", "earphones", "wireless", "bluetooth", "noise cancelling", "audio", "music", "sound"],
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "4K Smart TV",
        "category": "Electronics",
        "price": 599.99,
        "rating": 4,
        "reviews": 892,
        "description": "55-inch 4K UHD Smart TV with HDR and built-in streaming apps.",
        "features": ["4K Resolution", "HDR10", "Smart OS"],
        "keywords": ["television", "smart tv", "4k", "uhd", "hdr", "streaming", "entertainment", "home theater"],
        "image": "https://images.unsplash.com/photo-1571415060716-baff5f717c37?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Sony WH-1000XM5 Headphones",
        "category": "Electronics",
        "price": 349.99,
        "rating": 5,
        "reviews": 2105,
        "description": "Industry-leading noise cancellation with 30-hour battery life and crystal-clear audio.",
        "features": ["Bluetooth 5.2", "AI Noise Cancellation", "Touch Controls"],
        "keywords": ["sony", "headphones", "noise cancelling", "premium", "wireless", "bluetooth", "audio", "music"],
        "image": "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Apple iPhone 15 Pro",
        "category": "Electronics",
        "price": 999.00,
        "rating": 5,
        "reviews": 3500,
        "description": "A17 Pro chip, Super Retina XDR display, and advanced camera system.",
        "features": ["5G", "ProMotion Display", "48MP Camera"],
        "keywords": ["iphone", "smartphone", "apple", "mobile", "phone", "5g", "camera", "ios"],
        "image": "https://images.unsplash.com/photo-1695048134093-5d0d3f5f8a0c?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Samsung Galaxy S23 Ultra",
        "category": "Electronics",
        "price": 1199.99,
        "rating": 4,
        "reviews": 2876,
        "description": "200MP camera, Snapdragon 8 Gen 2, and S Pen support.",
        "features": ["200MP Camera", "S Pen", "8K Video"],
        "keywords": ["samsung", "galaxy", "android", "smartphone", "phone", "camera", "spen", "8k"],
        "image": "https://images.unsplash.com/photo-1676046187538-68269e8a1e6a?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Bose QuietComfort 45",
        "category": "Electronics",
        "price": 279.00,
        "rating": 4,
        "reviews": 1542,
        "description": "Premium noise-cancelling headphones with balanced sound.",
        "features": ["Triple-Mode ANC", "24hr Battery", "Lightweight"],
        "keywords": ["bose", "headphones", "quietcomfort", "noise cancelling", "wireless", "audio", "music"],
        "image": "https://images.unsplash.com/photo-1639754390580-2e7437267698?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "LG OLED C3 Series TV",
        "category": "Electronics",
        "price": 1499.99,
        "rating": 5,
        "reviews": 1320,
        "description": "65-inch OLED TV with AI-powered 4K and Dolby Vision.",
        "features": ["OLED Display", "AI Sound/Video", "Thin Design"],
        "keywords": ["lg", "oled", "television", "smart tv", "4k", "dolby vision", "home theater"],
        "image": "https://images.unsplash.com/photo-1593784991095-a205069470b6?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Google Pixel 8 Pro",
        "category": "Electronics",
        "price": 899.00,
        "rating": 4,
        "reviews": 980,
        "description": "Powered by Google Tensor G3 with advanced AI photography.",
        "features": ["Tensor G3", "Super Res Zoom", "30x Zoom"],
        "keywords": ["google", "pixel", "smartphone", "android", "camera", "ai", "phone"],
        "image": "https://images.unsplash.com/photo-1697898706716-3fd0a50f4d0b?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "JBL Flip 6 Portable Speaker",
        "category": "Electronics",
        "price": 129.95,
        "rating": 4,
        "reviews": 876,
        "description": "Waterproof Bluetooth speaker with deep bass and 12-hour playtime.",
        "features": ["IP67 Waterproof", "JBL Bass Radiator", "Party Mode"],
        "keywords": ["jbl", "speaker", "portable", "bluetooth", "wireless", "waterproof", "audio", "music"],
        "image": "https://images.unsplash.com/photo-1572569511254-d8f925fe2cbb?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Dell XPS 15 Laptop",
        "category": "Electronics",
        "price": 1599.99,
        "rating": 5,
        "reviews": 2045,
        "description": "15.6-inch 4K touchscreen laptop with Intel Core i9 and NVIDIA RTX graphics.",
        "features": ["4K OLED Display", "32GB RAM", "1TB SSD"],
        "keywords": ["dell", "xps", "laptop", "notebook", "ultrabook", "4k", "touchscreen", "gaming"],
        "image": "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    }
],
   "fashion": [
    {
        "name": "Organic Cotton T-Shirt",
        "category": "Fashion",
        "price": 29.99,
        "rating": 4,
        "reviews": 567,
        "description": "Soft, sustainable organic cotton t-shirt available in multiple colors.",
        "features": ["100% Organic Cotton", "Ethically Produced"],
        "keywords": ["t-shirt", "tee", "cotton", "organic", "basic", "casual", "sustainable", "eco-friendly"],
        "image": "https://images.unsplash.com/photo-1529374255404-311a2a4f1fd9?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Levi's 501 Original Jeans",
        "category": "Fashion",
        "price": 69.99,
        "rating": 5,
        "reviews": 1245,
        "description": "Classic straight-fit jeans with button fly and durable denim.",
        "features": ["100% Cotton", "Iconic Fit", "Machine Washable"],
        "keywords": ["jeans", "levis", "denim", "pants", "trousers", "straight fit", "classic", "button fly"],
        "image": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Nike Air Force 1 Sneakers",
        "category": "Fashion",
        "price": 99.99,
        "rating": 5,
        "reviews": 2300,
        "description": "Timeless white leather sneakers with Air cushioning.",
        "features": ["Leather Upper", "Air-Sole Unit", "Rubber Outsole"],
        "keywords": ["sneakers", "nike", "air force", "shoes", "footwear", "athletic", "casual", "white shoes"],
        "image": "https://images.unsplash.com/photo-1600269452121-4f2416e55c28?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Zara Oversized Blazer",
        "category": "Fashion",
        "price": 89.95,
        "rating": 4,
        "reviews": 876,
        "description": "Trendy oversized blazer with structured shoulders.",
        "features": ["Wool Blend", "Notch Lapel", "Two Buttons"],
        "keywords": ["blazer", "jacket", "oversized", "zara", "formal", "workwear", "office", "structured"],
        "image": "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Gucci GG Marmont Bag",
        "category": "Fashion",
        "price": 1290.00,
        "rating": 5,
        "reviews": 542,
        "description": "Luxury matelassé leather shoulder bag with GG logo.",
        "features": ["Leather", "Gold-Tone Hardware", "Adjustable Strap"],
        "keywords": ["handbag", "purse", "gucci", "designer", "luxury", "shoulder bag", "leather", "marmont"],
        "image": "https://images.unsplash.com/photo-1592078615290-033ee584e267?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Adidas Originals Track Pants",
        "category": "Fashion",
        "price": 59.99,
        "rating": 4,
        "reviews": 987,
        "description": "Classic track pants with signature three stripes.",
        "features": ["Polyester Blend", "Elastic Waistband", "Side Pockets"],
        "keywords": ["track pants", "sweatpants", "adidas", "athletic", "casual", "joggers", "sportswear", "three stripes"],
        "image": "https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Ray-Ban Aviator Sunglasses",
        "category": "Fashion",
        "price": 159.00,
        "rating": 5,
        "reviews": 2100,
        "description": "Iconic aviator sunglasses with UV protection.",
        "features": ["Polarized Lenses", "Metal Frame", "100% UV Protection"],
        "keywords": ["sunglasses", "rayban", "aviator", "eyewear", "sun glasses", "shades", "polarized", "uv protection"],
        "image": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "H&M Linen Shirt",
        "category": "Fashion",
        "price": 34.99,
        "rating": 4,
        "reviews": 654,
        "description": "Breathable linen shirt for a relaxed summer look.",
        "features": ["100% Linen", "Button-Down Collar", "Machine Washable"],
        "keywords": ["shirt", "linen", "summer", "casual", "hm", "button down", "breathable", "lightweight"],
        "image": "https://images.unsplash.com/photo-1527719327859-c6ce80353573?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Puma Running Shorts",
        "category": "Fashion",
        "price": 39.99,
        "rating": 4,
        "reviews": 432,
        "description": "Lightweight running shorts with moisture-wicking fabric.",
        "features": ["Polyester", "Elastic Waist", "Reflective Details"],
        "keywords": ["shorts", "running", "puma", "athletic", "workout", "gym", "sport", "moisture wicking"],
        "image": "https://images.unsplash.com/photo-1542272604-787c3835535d?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Calvin Klein Underwear Pack",
        "category": "Fashion",
        "price": 49.99,
        "rating": 5,
        "reviews": 1200,
        "description": "3-pack of cotton boxer briefs with logo waistband.",
        "features": ["Cotton Blend", "Breathable", "Multipack"],
        "keywords": ["underwear", "boxers", "briefs", "calvin klein", "under garments", "multipack", "cotton", "underwear set"],
        "image": "https://images.unsplash.com/photo-1582552938357-32b906df0cb1?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Dr. Martens 1460 Boots",
        "category": "Fashion",
        "price": 149.99,
        "rating": 5,
        "reviews": 1789,
        "description": "Classic leather combat boots with air-cushioned soles.",
        "features": ["Smooth Leather", "Goodyear Welt", "Slip-Resistant"],
        "keywords": ["boots", "doc martens", "combat boots", "leather", "ankle boots", "footwear", "durable", "slip resistant"],
        "image": "https://images.unsplash.com/photo-1560769629-975ec94e6a86?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Uniqlo Ultra Light Down Jacket",
        "category": "Fashion",
        "price": 79.90,
        "rating": 4,
        "reviews": 2100,
        "description": "Packable down jacket for cold weather.",
        "features": ["Water-Repellent", "Foldable", "Lightweight"],
        "keywords": ["jacket", "down", "puffer", "uniqlo", "winter", "coat", "outerwear", "packable"],
        "image": "https://images.unsplash.com/photo-1551232864-3f0890e580d9?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    }
],
    "home": [
    {
        "name": "Smart Air Fryer",
        "category": "Home & Kitchen",
        "price": 129.99,
        "rating": 5,
        "reviews": 892,
        "description": "Digital air fryer with smart presets and rapid air technology.",
        "features": ["Digital Controls", "Multiple Presets"],
        "keywords": ["air fryer", "fryer", "kitchen appliance", "healthy cooking", "countertop", "digital", "smart", "presets"],
        "image": "https://images.unsplash.com/photo-1615873968403-89e068629265?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Instant Pot Duo 7-in-1",
        "category": "Home & Kitchen",
        "price": 99.95,
        "rating": 5,
        "reviews": 4500,
        "description": "Pressure cooker, slow cooker, rice cooker, steamer, sauté pan, yogurt maker, and warmer.",
        "features": ["7-in-1 Functionality", "Stainless Steel Pot", "Easy Clean"],
        "keywords": ["instant pot", "pressure cooker", "slow cooker", "multi cooker", "rice cooker", "steamer", "yogurt maker", "kitchen essential"],
        "image": "https://images.unsplash.com/photo-1583623025817-18024011cebe?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Dyson V11 Cordless Vacuum",
        "category": "Home & Kitchen",
        "price": 499.99,
        "rating": 5,
        "reviews": 3200,
        "description": "Powerful cordless vacuum with intelligent suction and LCD screen.",
        "features": ["60min Runtime", "HEPA Filtration", "LCD Display"],
        "keywords": ["vacuum cleaner", "dyson", "cordless", "stick vacuum", "hepa", "pet hair", "powerful suction", "lcd"],
        "image": "https://images.unsplash.com/photo-1556740734-9f9ca6c5f2e4?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Keurig K-Classic Coffee Maker",
        "category": "Home & Kitchen",
        "price": 129.99,
        "rating": 4,
        "reviews": 2800,
        "description": "Single-serve coffee maker with multiple cup sizes.",
        "features": ["3 Brew Sizes", "Removable Drip Tray", "Fast Heating"],
        "keywords": ["coffee maker", "keurig", "k-cup", "single serve", "pod", "quick brew", "office", "breakroom"],
        "image": "https://images.unsplash.com/photo-1608355024227-8f7705e3d421?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Ninja Professional Blender",
        "category": "Home & Kitchen",
        "price": 89.99,
        "rating": 4,
        "reviews": 2100,
        "description": "1000W blender for smoothies, frozen drinks, and food processing.",
        "features": ["1000W Motor", "72oz Pitcher", "Dishwasher Safe"],
        "keywords": ["blender", "ninja", "smoothie", "food processor", "powerful", "frozen drinks", "kitchen gadget", "high speed"],
        "image": "https://images.unsplash.com/photo-1570585429632-e8b743a9a3e7?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Bissell CrossWave Vacuum Mop",
        "category": "Home & Kitchen",
        "price": 229.99,
        "rating": 4,
        "reviews": 1500,
        "description": "Vacuum and wash floors at the same time with this 2-in-1 machine.",
        "features": ["Multi-Surface Cleaning", "Washable Filters", "Large Tank"],
        "keywords": ["vacuum mop", "floor cleaner", "bissell", "hardwood", "tile", "2-in-1", "pet friendly", "deep clean"],
        "image": "https://images.unsplash.com/photo-1600880292203-757bb62b4baf?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Lodge Cast Iron Skillet",
        "category": "Home & Kitchen",
        "price": 29.99,
        "rating": 5,
        "reviews": 9800,
        "description": "Pre-seasoned cast iron skillet for stovetop and oven cooking.",
        "features": ["10.25-inch", "Pre-Seasoned", "Durable"],
        "keywords": ["cast iron", "skillet", "pan", "lodge", "cookware", "oven safe", "non-stick", "seasoned"],
        "image": "https://images.unsplash.com/photo-1582515073490-39981397c445?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "iRobot Roomba i3+ Robot Vacuum",
        "category": "Home & Kitchen",
        "price": 399.99,
        "rating": 4,
        "reviews": 1800,
        "description": "Self-emptying robot vacuum with smart mapping.",
        "features": ["Self-Emptying Base", "Wi-Fi Connected", "Multi-Surface Cleaning"],
        "keywords": ["robot vacuum", "roomba", "self emptying", "smart", "wi-fi", "automatic", "hands-free", "pet hair"],
        "image": "https://images.unsplash.com/photo-1588943211346-0908a1fb0b01?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    }
],
    
    "beauty": [
    {
        "name": "Vitamin C Serum",
        "category": "Beauty",
        "price": 24.99,
        "rating": 4,
        "reviews": 1345,
        "description": "Brightening vitamin C serum with hyaluronic acid.",
        "features": ["Brightening", "Hydrating"],
        "keywords": ["serum", "vitamin c", "brightening", "skincare", "face", "anti-aging", "glow", "hyaluronic acid"],
        "image": "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
        "choice": "Reliable"
    },
    {
        "name": "CeraVe Moisturizing Cream",
        "category": "Beauty",
        "price": 16.99,
        "rating": 5,
        "reviews": 8900,
        "description": "Dermatologist-recommended moisturizer with ceramides.",
        "features": ["Fragrance-Free", "Non-Comedogenic", "24hr Hydration"],
        "keywords": ["moisturizer", "cerave", "cream", "dry skin", "sensitive", "ceramides", "dermatologist", "hydration"],
        "image": "https://images.unsplash.com/photo-1625772452859-1c03d5bf1137?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
        "choice": "Reliable"
    },
    {
        "name": "Maybelline Sky High Mascara",
        "category": "Beauty",
        "price": 9.99,
        "rating": 4,
        "reviews": 4500,
        "description": "Lengthening mascara for dramatic lashes.",
        "features": ["Washable", "Clump-Free", "Vitamin B5"],
        "keywords": ["mascara", "maybelline", "lengthening", "eyelashes", "volumizing", "drugstore", "makeup", "waterproof"],
        "image": "https://images.unsplash.com/photo-1625772452859-1c03d5bf1137?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
        "choice": "Reliable"
    },
    {
        "name": "The Ordinary Niacinamide Serum",
        "category": "Beauty",
        "price": 12.90,
        "rating": 4,
        "reviews": 6800,
        "description": "Oil-control serum with 10% niacinamide and zinc.",
        "features": ["Blemish Control", "Minimizes Pores", "Vegan"],
        "keywords": ["niacinamide", "serum", "the ordinary", "acne", "pores", "oil control", "zinc", "skincare"],
        "image": "https://images.unsplash.com/photo-1571781926291-c477ebfd024b?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
        "choice": "Reliable"
    },
    {
        "name": "La Mer Crème de la Mer",
        "category": "Beauty",
        "price": 385.00,
        "rating": 5,
        "reviews": 1200,
        "description": "Iconic luxury moisturizer with miracle broth.",
        "features": ["Anti-Aging", "Rich Texture", "Signature Scent"],
        "keywords": ["la mer", "luxury", "moisturizer", "cream", "anti-aging", "miracle broth", "premium", "skincare"],
        "image": "https://images.unsplash.com/photo-1610548822783-33fb5cb0e3ff?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
        "choice": "Luxury"
    },
    {
        "name": "Dior Lip Glow Oil",
        "category": "Beauty",
        "price": 38.00,
        "rating": 5,
        "reviews": 2400,
        "description": "Hydrating lip oil with sheer tint and cherry oil.",
        "features": ["Non-Sticky", "Plumping Effect", "Luxury Packaging"],
        "keywords": ["dior", "lip oil", "gloss", "hydrating", "plumping", "sheer", "luxury", "makeup"],
        "image": "https://images.unsplash.com/photo-1586495777744-4413f21062fa?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
        "choice": "Luxury"
    },
    {
        "name": "Drunk Elephant Retinol Cream",
        "category": "Beauty",
        "price": 78.00,
        "rating": 4,
        "reviews": 3200,
        "description": "Gentle retinol cream for night-time renewal.",
        "features": ["1% Retinol", "Peptide Complex", "Vegan"],
        "keywords": ["retinol", "drunk elephant", "night cream", "anti-aging", "renewal", "vegan", "skincare", "peptide"],
        "image": "https://images.unsplash.com/photo-1571781926291-c477ebfd024b?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
        "choice": "Luxury"
    },
    {
        "name": "Charlotte Tilbury Pillow Talk Lipstick",
        "category": "Beauty",
        "price": 34.00,
        "rating": 5,
        "reviews": 5100,
        "description": "Cult-favorite nude-pink lipstick with creamy finish.",
        "features": ["Hydrating", "Universal Shade", "Rose Gold Packaging"],
        "keywords": ["charlotte tilbury", "lipstick", "pillow talk", "nude", "pink", "creamy", "luxury", "makeup"],
        "image": "https://images.unsplash.com/photo-1625772452859-1c03d5bf1137?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
        "choice": "Luxury"
    },
    {
        "name": "Tom Ford Oud Wood Perfume",
        "category": "Beauty",
        "price": 390.00,
        "rating": 5,
        "reviews": 980,
        "description": "Luxury unisex fragrance with woody oriental notes.",
        "features": ["Long-Lasting", "Exotic Ingredients", "Signature Scent"],
        "keywords": ["tom ford", "perfume", "fragrance", "oud", "woody", "luxury", "unisex", "long lasting"],
        "image": "https://images.unsplash.com/photo-1594035910387-fea47794261f?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
        "choice": "Luxury"
    }
],

    "sports": [
    {
        "name": "Yoga Mat",
        "category": "Sports & Fitness",
        "price": 49.99,
        "rating": 4,
        "reviews": 723,
        "description": "Eco-friendly non-slip yoga mat with alignment markers.",
        "features": ["Non-slip", "Eco-friendly"],
        "keywords": ["yoga", "exercise mat", "pilates", "workout", "fitness", "non-slip", "eco", "alignment"],
        "image": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Adjustable Dumbbell Set",
        "category": "Sports & Fitness",
        "price": 199.99,
        "rating": 5,
        "reviews": 1542,
        "description": "Space-saving adjustable dumbbells from 5-50 lbs with quick-change dial.",
        "features": ["5-50 lbs range", "Quick-change weights", "Non-slip grip"],
        "keywords": ["dumbbells", "weights", "home gym", "strength training", "adjustable", "fitness", "workout", "compact"],
        "image": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Running Shoes",
        "category": "Sports & Fitness",
        "price": 129.99,
        "rating": 4,
        "reviews": 2876,
        "description": "Lightweight running shoes with responsive cushioning for all terrains.",
        "features": ["Breathable mesh", "Shock absorption", "Arch support"],
        "keywords": ["running", "sneakers", "athletic shoes", "jogging", "trail running", "cushioned", "breathable", "support"],
        "image": "https://images.unsplash.com/photo-1460353581641-37baddab0fa2?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Foldable Exercise Bike",
        "category": "Sports & Fitness",
        "price": 249.99,
        "rating": 4,
        "reviews": 932,
        "description": "Compact stationary bike with 8 resistance levels and LCD monitor.",
        "features": ["Space-saving design", "Quiet operation", "Heart rate monitor"],
        "keywords": ["exercise bike", "stationary bike", "cycling", "cardio", "home gym", "folding", "resistance", "fitness"],
        "image": "https://images.unsplash.com/photo-1538805060514-97d9cc17730c?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Basketball",
        "category": "Sports & Fitness",
        "price": 34.99,
        "rating": 5,
        "reviews": 1245,
        "description": "Official size 7 basketball with durable composite leather cover.",
        "features": ["Indoor/outdoor", "Grip channels", "Moisture-wicking"],
        "keywords": ["basketball", "sports ball", "nba", "outdoor", "indoor", "composite", "durable", "grip"],
        "image": "https://images.unsplash.com/photo-1546519638-68e109498ffc?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Resistance Bands Set",
        "category": "Sports & Fitness",
        "price": 29.99,
        "rating": 4,
        "reviews": 2103,
        "description": "5-piece latex resistance bands with handles for full-body workouts.",
        "features": ["5 tension levels", "Door anchor included", "Portable"],
        "keywords": ["resistance bands", "exercise bands", "workout", "strength training", "portable", "home gym", "tension", "fitness"],
        "image": "https://images.unsplash.com/photo-1595079835353-8a17e6f317c0?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Golf Club Set",
        "category": "Sports & Fitness",
        "price": 399.99,
        "rating": 4,
        "reviews": 587,
        "description": "Complete 10-piece golf set with bag for beginners and intermediates.",
        "features": ["Driver, irons, putter", "Stand bag", "Head covers"],
        "keywords": ["golf clubs", "golf set", "beginner", "irons", "driver", "putter", "golf bag", "stand bag"],
        "image": "https://images.unsplash.com/photo-1535131749006-b7f58c99034d?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Smart Jump Rope",
        "category": "Sports & Fitness",
        "price": 59.99,
        "rating": 4,
        "reviews": 876,
        "description": "Bluetooth-enabled jump rope with app connectivity to track workouts.",
        "features": ["Counts jumps", "Calorie tracking", "Adjustable length"],
        "keywords": ["jump rope", "skipping rope", "cardio", "workout", "smart", "bluetooth", "fitness tracker", "adjustable"],
        "image": "https://images.unsplash.com/photo-1538805060514-97d9cc17730c?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    }
],
    
    "books": [
    {
        "name": "Bestselling Novel",
        "category": "Books",
        "price": 14.99,
        "rating": 5,
        "reviews": 2314,
        "description": "The latest bestselling novel from award-winning author.",
        "features": ["Hardcover", "Bestseller"],
        "keywords": ["fiction", "contemporary", "award-winning", "page-turner", "literary", "popular", "critically acclaimed", "book club"],
        "image": "https://images.unsplash.com/photo-1544947950-fa07a98d237f?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Atomic Habits",
        "category": "Books",
        "price": 11.98,
        "rating": 5,
        "reviews": 45000,
        "description": "James Clear's guide to building good habits and breaking bad ones.",
        "features": ["Self-Help", "Paperback"],
        "keywords": ["self-improvement", "productivity", "psychology", "behavior", "motivation", "success", "personal growth", "routine"],
        "image": "https://images.unsplash.com/photo-1589998059171-988d887df646?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "The Midnight Library",
        "category": "Books",
        "price": 13.50,
        "rating": 4,
        "reviews": 12500,
        "description": "A novel about regrets and second chances by Matt Haig.",
        "features": ["Fiction", "NYT Bestseller"],
        "keywords": ["speculative fiction", "life choices", "alternate lives", "emotional", "thought-provoking", "redemption", "what-if", "depression"],
        "image": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Sapiens: A Brief History of Humankind",
        "category": "Books",
        "price": 16.99,
        "rating": 5,
        "reviews": 32000,
        "description": "Yuval Noah Harari's exploration of human history.",
        "features": ["Non-Fiction", "Illustrated"],
        "keywords": ["anthropology", "evolution", "civilization", "big history", "science", "philosophy", "human origins", "cognitive revolution"],
        "image": "https://images.unsplash.com/photo-1589998059171-988d887df646?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "The Very Hungry Caterpillar",
        "category": "Books",
        "price": 7.99,
        "rating": 5,
        "reviews": 8900,
        "description": "Classic children's book by Eric Carle.",
        "features": ["Board Book", "Ages 0-3"],
        "keywords": ["picture book", "toddler", "early learning", "colors", "numbers", "metamorphosis", "bedtime story", "interactive"],
        "image": "https://images.unsplash.com/photo-1592496431122-2349e0fbc666?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Dune",
        "category": "Books",
        "price": 9.99,
        "rating": 5,
        "reviews": 18700,
        "description": "Frank Herbert's epic science fiction masterpiece.",
        "features": ["Sci-Fi", "Movie Tie-In"],
        "keywords": ["space opera", "desert planet", "political intrigue", "chosen one", "ecology", "spice", "futuristic", "saga"],
        "image": "https://images.unsplash.com/photo-1544947950-fa07a98d237f?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "The Silent Patient",
        "category": "Books",
        "price": 12.99,
        "rating": 4,
        "reviews": 9800,
        "description": "Psychological thriller with a shocking twist.",
        "features": ["Mystery", "Hardcover"],
        "keywords": ["psychological", "suspense", "unreliable narrator", "mental health", "crime", "plot twist", "page-turner", "therapist"],
        "image": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Cooking for Beginners",
        "category": "Books",
        "price": 19.99,
        "rating": 4,
        "reviews": 3200,
        "description": "Essential recipes and techniques for new cooks.",
        "features": ["Spiral Bound", "Step-by-Step Photos"],
        "keywords": ["cookbook", "easy recipes", "kitchen basics", "meal prep", "how-to", "culinary", "beginner chef", "home cooking"],
        "image": "https://images.unsplash.com/photo-1544947950-fa07a98d237f?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    }
],
    "toys": [
    {
        "name": "Educational STEM Toy",
        "category": "Toys & Games",
        "price": 39.99,
        "rating": 5,
        "reviews": 456,
        "description": "Award-winning STEM toy that teaches coding basics.",
        "features": ["Educational", "Coding Basics"],
        "keywords": ["adventure tech", "robot explorer", "science quest", "inventor kit", "digital adventure", "future builder", "tech hero", "coding adventure"],
        "image": "https://images.unsplash.com/photo-1596461404969-9ae70f2830c1?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "LEGO Classic Creative Brick Box",
        "category": "Toys & Games",
        "price": 29.99,
        "rating": 5,
        "reviews": 12500,
        "description": "790-piece LEGO set for unlimited creative building.",
        "features": ["Ages 4+", "Storage Included"],
        "keywords": ["castle adventure", "space explorer", "jungle quest", "pirate ship", "dinosaur world", "character builder", "story creator", "imagination land"],
        "image": "https://images.unsplash.com/photo-1585076641399-5c06d1b3365f?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Nerf Elite 2.0 Blaster",
        "category": "Toys & Games",
        "price": 24.99,
        "rating": 4,
        "reviews": 7800,
        "description": "Motorized dart blaster with 40-dart capacity.",
        "features": ["Ages 8+", "Includes 40 Darts"],
        "keywords": ["battle adventure", "superhero gear", "spy mission", "zombie defense", "space ranger", "action hero", "secret agent", "adventure warrior"],
        "image": "https://images.unsplash.com/photo-1596461404969-9ae70f2830c1?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Baby Einstein Take Along Tunes",
        "category": "Toys & Games",
        "price": 12.99,
        "rating": 5,
        "reviews": 9800,
        "description": "Musical toy with lights for infant development.",
        "keywords": ["animal friends", "musical adventure", "first explorer", "baby hero", "discovery pal", "learning buddy", "tiny adventurer", "character companion"],
        "image": "https://images.unsplash.com/photo-1594782915050-986d661ab828?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Barbie Dreamhouse",
        "category": "Toys & Games",
        "price": 199.99,
        "rating": 4,
        "reviews": 3200,
        "description": "3-story dollhouse with elevator and pool.",
        "features": ["75+ Accessories", "Lights & Sounds"],
        "keywords": ["character world", "fashion adventure", "celebrity life", "storytelling", "roleplay kingdom", "dream adventure", "friendship tales", "glamour explorer"],
        "image": "https://images.unsplash.com/photo-1596461404969-9ae70f2830c1?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Pokémon Trading Card Game Set",
        "category": "Toys & Games",
        "price": 19.99,
        "rating": 5,
        "reviews": 5600,
        "description": "Starter deck for the popular trading card game.",
        "features": ["60 Cards", "Ages 6+"],
        "keywords": ["pokemon adventure", "character battle", "quest cards", "pocket monsters", "gotta catch em all", "trainer journey", "gym challenge", "legendary hunt"],
        "image": "https://images.unsplash.com/photo-1611250282006-4484dd3fba6b?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Melissa & Doug Wooden Puzzle",
        "category": "Toys & Games",
        "price": 14.99,
        "rating": 5,
        "reviews": 8700,
        "description": "24-piece wooden animal puzzle for toddlers.",
        "features": ["Ages 2+", "Non-Toxic"],
        "keywords": ["safari adventure", "animal friends", "jungle quest", "farmyard pals", "discovery puzzle", "character learning", "wild explorer", "tiny adventurer"],
        "image": "https://images.unsplash.com/photo-1594782915050-986d661ab828?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    },
    {
        "name": "Hot Wheels Ultimate Garage",
        "category": "Toys & Games",
        "price": 59.99,
        "rating": 4,
        "reviews": 2100,
        "description": "Multi-level car playset with elevator and launcher.",
        "features": ["5+ Cars Included", "Ages 4+"],
        "keywords": ["race adventure", "speed challenge", "stunt driver", "car character", "track explorer", "velocity quest", "garage hero", "adventure track"],
        "image": "https://images.unsplash.com/photo-1596461404969-9ae70f2830c1?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
    }
],
    "grocery": [
        {
            "name": "Organic Coffee Beans",
            "category": "Grocery",
            "price": 12.99,
            "rating": 4,
            "reviews": 892,
            "description": "Premium organic coffee beans, fair trade certified.",
            "features": ["Organic", "Fair Trade"],
            "image": "https://images.unsplash.com/photo-1515446134809-993c501ca304?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
        },
        {
            "name": "Organic Honey",
            "category": "Grocery",
            "price": 8.99,
            "rating": 5,
            "reviews": 2300,
            "description": "Raw, unfiltered honey from local apiaries.",
            "features": ["16oz Jar", "Non-GMO"],
            "image": "https://images.unsplash.com/photo-1587049352851-8d4e89133924?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
        },
        {
            "name": "Extra Virgin Olive Oil",
            "category": "Grocery",
            "price": 15.99,
            "rating": 5,
            "reviews": 4500,
            "description": "Cold-pressed olive oil from Italy.",
            "features": ["1 Liter", "First Cold Press"],
            "image": "https://images.unsplash.com/photo-1552581234-26160f608093?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
        },
        {
            "name": "Organic Quinoa",
            "category": "Grocery",
            "price": 6.99,
            "rating": 4,
            "reviews": 3200,
            "description": "Protein-rich ancient grain, perfect for salads.",
            "features": ["16oz", "Gluten-Free"],
            "image": "https://images.unsplash.com/photo-1518977676601-b53f82aba655?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
        },
        {
            "name": "Dark Chocolate Bars (Pack of 12)",
            "category": "Grocery",
            "price": 18.99,
            "rating": 5,
            "reviews": 5600,
            "description": "70% cocoa dark chocolate with sea salt.",
            "features": ["Vegan", "Non-GMO"],
            "image": "https://images.unsplash.com/photo-1493925410344-008a2d663cdf?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
        },
        {
            "name": "Organic Almond Butter",
            "category": "Grocery",
            "price": 9.99,
            "rating": 4,
            "reviews": 2100,
            "description": "Creamy almond butter with no added sugar.",
            "features": ["16oz Jar", "Keto-Friendly"],
            "image": "https://images.unsplash.com/photo-1612528443702-f6741f70a049?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
        },
        {
            "name": "Artisanal Sea Salt",
            "category": "Grocery",
            "price": 5.99,
            "rating": 5,
            "reviews": 1200,
            "description": "Hand-harvested sea salt with natural minerals.",
            "features": ["8oz", "No Additives"],
            "image": "https://images.unsplash.com/photo-1518977676601-b53f82aba655?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
        },
        {
            "name": "Organic Free-Range Eggs",
            "category": "Grocery",
            "price": 4.99,
            "rating": 5,
            "reviews": 4500,
            "description": "Dozen large eggs from pasture-raised chickens.",
            "features": ["12 Count", "Certified Humane"],
            "image": "https://images.unsplash.com/photo-1587486913049-53fc88980cfc?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
        }
    ],
    
    }


# ===== EXPERT SYSTEM =====
class RecommendationEngine:
    def __init__(self):
        self.rules = [
            self._exact_match_rule,
            self._keyword_match_rule,
            self._name_preference_rule,
            self._desc_preference_rule,
            self._feature_preference_rule,
            self._budget_rule,
            self._popular_rule
        ]
    
    def recommend(self, products, budget, preferences):
        scored_products = []
        pref_lower = preferences.lower().strip() if preferences else ""
        
        for product in products:
            score = 0
            match_types = []
            
            # Apply all rules
            for rule in self.rules:
                rule_score, rule_match = rule(product, budget, pref_lower)
                score += rule_score
                if rule_match:
                    match_types.append(rule_match)
            
            if score > 0:
                scored_products.append({
                    **product,
                    "score": round(score, 2),
                    "match_types": match_types
                })
        
        # Sort by score descending
        return sorted(scored_products, key=lambda x: x['score'], reverse=True)
    
    def _exact_match_rule(self, product, budget, pref_lower):
        if not pref_lower:
            return 0, None
            
        # Check if preference exactly matches any keyword
        if 'keywords' in product and pref_lower in [k.lower() for k in product['keywords']]:
            return (10 + (product['rating'] * 0.5) + (min(product['reviews'], 5000) * 0.001), "exact_keyword_match")
        return 0, None
    
    def _keyword_match_rule(self, product, budget, pref_lower):
        if not pref_lower:
            return 0, None
            
        # Check if preference is contained in any keyword
        if 'keywords' in product and any(pref_lower in k.lower() for k in product['keywords']):
            return (8 + (product['rating'] * 0.5) + (min(product['reviews'], 5000) * 0.001), "partial_keyword_match")
        return 0, None
    
    def _name_preference_rule(self, product, budget, pref_lower):
        if not pref_lower:
            return 0, None
            
        if pref_lower in product['name'].lower():
            return (7 + (product['rating'] * 0.5) + (min(product['reviews'], 5000) * 0.001), "name_match")
        return 0, None
    
    def _desc_preference_rule(self, product, budget, pref_lower):
        if not pref_lower:
            return 0, None
            
        if pref_lower in product['description'].lower():
            return (6 + (product['rating'] * 0.5) + (min(product['reviews'], 5000) * 0.001), "desc_match")
        return 0, None
    
    def _feature_preference_rule(self, product, budget, pref_lower):
        if not pref_lower:
            return 0, None
            
        if any(pref_lower in feat.lower() for feat in product['features']):
            return (5 + (product['rating'] * 0.5) + (min(product['reviews'], 5000) * 0.001), "feature_match")
        return 0, None
    
    def _budget_rule(self, product, budget, pref_lower):
        price = product['price']
        if (
            (budget == "low" and price < 50) or
            (budget == "medium" and 50 <= price <= 200) or
            (budget == "high" and 200 < price <= 500) or
            (budget == "premium" and price > 500)
        ):
            return (5 + (product['rating'] * 0.75) + (min(product['reviews'], 5000) * 0.001), f"budget_{budget}")
        return 0, None
    
    def _popular_rule(self, product, budget, pref_lower):
        if product['rating'] >= 4.5 and product['reviews'] > 2000:
            return (7 + (min(product['reviews'], 5000) * 0.001), "highly_rated")
        return 0, None



# ===== FLASK ROUTES =====
@app.route('/')
def index():
    return render_template('index.html')

# Replace this route with your enhanced version
@app.route('/get_recommendations', methods=['POST'])
def get_recommendations():
    data = request.json
    
    category = data.get('category', 'all')
    budget = data.get('budget', 'medium')
    preferences = data.get('preferences', '').strip()
    
    # Get products
    if category == 'all':
        products = []
        for cat_products in product_database.values():
            products.extend(cat_products)
    else:
        products = product_database.get(category, [])
    
    # Filter by budget first
    budget_ranges = {
        'low': (0, 50),
        'medium': (50, 200),
        'high': (200, 500),
        'premium': (500, float('inf'))
    }
    min_price, max_price = budget_ranges.get(budget, (0, float('inf')))
    budget_filtered = [p for p in products if min_price <= p['price'] <= max_price]
    
    # Enhanced recommendation logic
    if not preferences:
        # If no preferences, return top rated in budget
        recommendations = sorted(
            budget_filtered, 
            key=lambda x: (x['rating'], x['reviews']), 
            reverse=True
        )[:8]
        return jsonify({
            "status": "success",
            "recommendations": recommendations,
            "message": "Top rated products in your budget"
        })
    
    # Normalize preferences
    pref_lower = preferences.lower()
    pref_words = set(pref_lower.split())  # Split into individual words
    
    scored_products = []
    for product in budget_filtered:
        score = 0
        match_details = []
        
        # Normalize product data for comparison
        name_lower = product['name'].lower()
        desc_lower = product['description'].lower()
        features_lower = [f.lower() for f in product.get('features', [])]
        keywords_lower = [k.lower() for k in product.get('keywords', [])]
        
        # 1. Check for exact preference match in keywords (highest priority)
        if any(pref_lower == kw for kw in keywords_lower):
            score += 15
            match_details.append("exact_keyword_match")
        
        # 2. Check if preference is contained in product name
        if pref_lower in name_lower:
            score += 12
            match_details.append("name_contains_preference")
        
        # 3. Check if preference is contained in description
        if pref_lower in desc_lower:
            score += 10
            match_details.append("desc_contains_preference")
        
        # 4. Check for individual word matches in keywords
        keyword_word_matches = [word for word in pref_words 
                              if any(word in kw for kw in keywords_lower)]
        if keyword_word_matches:
            score += 8 + len(keyword_word_matches) * 2
            match_details.append(f"keyword_word_matches:{','.join(keyword_word_matches)}")
        
        # 5. Check for individual word matches in name
        name_word_matches = [word for word in pref_words if word in name_lower]
        if name_word_matches:
            score += 6 + len(name_word_matches) * 1.5
            match_details.append(f"name_word_matches:{','.join(name_word_matches)}")
        
        # 6. Check for individual word matches in description
        desc_word_matches = [word for word in pref_words if word in desc_lower]
        if desc_word_matches:
            score += 5 + len(desc_word_matches) * 1
            match_details.append(f"desc_word_matches:{','.join(desc_word_matches)}")
        
        # 7. Check for individual word matches in features
        feature_word_matches = []
        for feat in features_lower:
            feature_word_matches.extend(word for word in pref_words if word in feat)
        if feature_word_matches:
            score += 4 + len(feature_word_matches) * 1
            match_details.append(f"feature_word_matches:{','.join(feature_word_matches)}")
        
        # Add rating and popularity factors (if any matches found)
        if match_details:
            score += product['rating'] * 0.5  # Higher rated products get bonus
            score += min(product['reviews'], 10000) / 2000  # Popular products get bonus
            
            scored_products.append({
                **product,
                "score": round(score, 2),
                "match_details": match_details
            })
    
    # Sort by score descending
    recommendations = sorted(scored_products, key=lambda x: x['score'], reverse=True)[:8]
    
    # If no matches found, try a more flexible search
    if not recommendations:
        print("No direct matches found, trying more flexible search")
        flexible_matches = []
        for product in budget_filtered:
            # Check if any preference word appears anywhere in product data
            product_text = ' '.join([
                product['name'].lower(),
                product['description'].lower(),
                ' '.join(f.lower() for f in product.get('features', [])),
                ' '.join(k.lower() for k in product.get('keywords', []))
            ])
            
            matches = [word for word in pref_words if word in product_text]
            if matches:
                score = len(matches) * 3 + product['rating'] * 0.5
                flexible_matches.append({
                    **product,
                    "score": round(score, 2),
                    "match_details": [f"flexible_match:{','.join(matches)}"]
                })
        
        recommendations = sorted(flexible_matches, key=lambda x: x['score'], reverse=True)[:8]
    
    # Final fallback - top rated in budget if still no matches
    if not recommendations:
        print("No matches at all, returning top rated")
        recommendations = sorted(
            budget_filtered, 
            key=lambda x: (x['rating'], x['reviews']), 
            reverse=True
        )[:8]
    
    return jsonify({
        "status": "success",
        "recommendations": recommendations,
        "engine": "enhanced_preference_matching_v2"
    })
if __name__ == '__main__':
    app.run(debug=True)