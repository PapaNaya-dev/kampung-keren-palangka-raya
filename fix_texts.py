import json

def fix_texts():
    with open('data/kawasan.geojson', 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for feat in data['features']:
        p = feat['properties']
        kw = p['Kawasan']
        
        # Complete the texts based on context
        if kw == 'Kawasan IV':
            p['Call_to_Ac'] = '"Bangkitkan potensi terpendam \'Kampung Kriya\'!"\nKawasan ini memiliki denyut nadi ekonomi dari para pengrajin anyaman bambu dan purun yang pemasarannya belum optimal. Kawasan IV membutuhkan sentuhan magis Anda untuk merombak infrastruktur dasar yang masih tertinggal agar roda ekonomi warga dapat berputar maksimal.'
        elif kw == 'Kawasan VI':
            p['Call_to_Ac'] = '"Sinergikan denyut nadi ekonomi komersial dan kelestarian lingkungan!"\nBerada di lokasi strategis Kelurahan Palangka dengan potensi UMKM unggulan seperti Batik Bahalap dan Amplang. Namun, tata kelola air limbah dan ancaman kebakaran di permukiman padat ini membutuhkan solusi desain tata ruang yang inovatif dan terpadu.'
        elif kw == 'Kawasan III':
            p['Call_to_Ac'] = '"Bawa napas baru untuk permukiman di jantung kota!"\nKawasan ini memiliki peluang besar untuk pengembangan Urban Farming dan perniagaan. Namun, para warga masih menghadapi tantangan serius pada pemenuhan air bersih, sistem drainase, dan penataan letak bangunan yang padat.'
        elif kw == 'Kawasan II':
            p['Call_to_Ac'] = '"Dari permukiman padat menjadi sentra ekonomi kreatif!"\nBerada di wilayah yang berkembang pesat, kawasan ini kaya akan potensi UMKM kriya dan kuliner khas Dayak. Tantangan utama Anda: mengatasi krisis pengelolaan persampahan (67%) dan menata ruang permukiman agar lebih sehat dan aman.'
        elif kw == 'Kawasan V':
            p['Call_to_Ac'] = '"Eksplorasi pesona vernakular Kahayan Riverside!"\nPahandut Seberang memiliki keunikan budaya permukiman tepi sungai yang luar biasa dan sangat layak dijadikan destinasi wisata air. Tantangan Anda di sini adalah merancang infrastruktur pendukung pariwisata yang tahan banjir dan ramah lingkungan.'
        elif kw == 'Kawasan VII':
            p['Call_to_Ac'] = '"Harmonisasi episentrum niaga dengan ruang hidup yang sehat!"\nMengusung potensi besar sebagai pusat jasa dan kerajinan lokal khas Palangka Raya, Kawasan VII menanti inovasi tata ruang Anda. Bagaimana Anda menyelaraskan aktivitas ekonomi warga yang tinggi dengan penyediaan sanitasi dasar yang layak?'
        elif kw == 'Kawasan VIII':
            p['Call_to_Ac'] = '"Optimalisasi ruang cerdas di kawasan padat dan strategis!"\nDikelilingi oleh pusat aktivitas dan kekayaan UMKM lokal, Kawasan VIII menantang Anda untuk menghadirkan konsep tata ruang cerdas di lahan terbatas. Tunjukkan bagaimana ide rancangan tapak Anda dapat meningkatkan kualitas hidup warga di tengah tingginya kepadatan penduduk.'
        elif kw == 'Kawasan I':
            p['Call_to_Ac'] = '"Wujudkan pesona pesisir Air Hitam yang aman dan asri!"\nKawasan ini menyimpan berlian ekowisata Kereng Bangkirai dan menjadi gerbang Taman Nasional Sebangau. Namun, mimpi desa wisata ini terancam oleh risiko kebakaran yang sangat tinggi (100%) dan tata kelola lingkungan yang perlu segera dibenahi.'
        
    with open('data/kawasan.geojson', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    fix_texts()
    print("Texts updated successfully.")
