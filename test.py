import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

st.title('体質傾向チェックWEBアプリ')
st.caption('日常的に感じる症状や生活習慣をもとに気・血・水の状態をチェックするアプリです。')
st.text('以下の質問から該当する箇所を選択して下さい')
count = np.zeros(8)

with st.form("my_form"):
    q1 = st.checkbox('胸やお腹が張って苦しいことが多い')
    if q1:
        count += np.array([0, 0, 0, 0, 3, 1, 0, 1])
        print(count)
    q2 = st.checkbox('イライラしやすく怒りっぽい')
    if q2:
        count += np.array([0, 0, 0, 2, 3, 0, 0, 0])
        print(count)
    q3 = st.checkbox('不眠になりやすい')
    if q3:
        count += np.array([0, 0, 3, 2, 3, 0, 1, 0])
        print(count)
    q4 = st.checkbox('黄色い粘り気のある痰や鼻水がよく出る')
    if q4:
        count += np.array([0, 0, 0, 0, 0, 3, 0, 0])
        print(count)
    q5 = st.checkbox('尿がよく濃い黄色になる')
    if q5:
        count += np.array([0, 0, 0, 1, 0, 3, 0, 0])
        print(count)
    q6 = st.checkbox('肩が凝りやすい')
    if q6:
        count += np.array([0, 0, 0, 0, 3, 1, 3, 1])
        print(count)
    q7 = st.checkbox('唇や歯茎の色が紫に近い')
    if q7:
        count += np.array([0, 0, 0, 0, 0, 0, 3, 0])
        print(count)
    q8 = st.checkbox('頭が重く感じられることが多い')
    if q8:
        count += np.array([1, 0, 0, 0, 0, 1, 1, 3])
        print(count)
    q9 = st.checkbox('雨の日や湿度の高い日は体調が悪くなりがち')
    if q9:
        count += np.array([0, 0, 0, 0, 0, 1, 0, 3])
        print(count)
    q10 = st.checkbox('皮膚や乾燥してカサカサしている')
    if q10:
        count += np.array([0, 0, 3, 1, 0, 0, 1, 0])
        print(count)
    q11 = st.checkbox('舌の縁がギザギザになっている')
    if q11:
        count += np.array([3, 1, 0, 0, 0, 0, 0, 2])
        print(count)
    q12 = st.checkbox('舌苔がびっしりついていて厚みがある')
    if q12:
        count += np.array([2, 1, 0, 0, 0, 2, 0, 2])
        print(count)
    q13 = st.checkbox('舌の裏の静脈が太く膨らんで見える')
    if q13:
        count += np.array([0, 0, 0, 0, 0, 0, 3, 0])
        print(count)
    q14 = st.checkbox('食が細い方だ')
    if q14:
        count += np.array([3, 0, 0, 0, 0, 0, 0, 0])
        print(count)
    q15 = st.checkbox('下痢や軟便になることがよくある')
    if q15:
        count += np.array([3, 1, 0, 0, 0, 1, 0, 2])
        print(count)
    q16 = st.checkbox('よく腰や膝に疲れや脱力感を覚える')
    if q16:
        count += np.array([0, 3, 0, 0, 0, 0, 0, 0])
        print(count)
    q17 = st.checkbox('むくみを感じることが多い')
    if q17:
        count += np.array([0, 3, 0, 0, 0, 0, 0, 2])
        print(count)
    q18 = st.checkbox('髪の毛が抜けやすい')
    if q18:
        count += np.array([0, 2, 3, 0, 0, 1, 1, 0])
        print(count)
    q19 = st.checkbox('目が疲れたり乾燥しやすい')
    if q19:
        count += np.array([0, 0, 3, 1, 0, 0, 0, 0])
        print(count)
    q20 = st.checkbox('筋肉が痙攣したり、つりやすい')
    if q20:
        count += np.array([0, 0, 3, 1, 1, 0, 0, 0])
        print(count)
    q21 = st.checkbox('体温は高くないが、体が熱っぽく感じる')
    if q21:
        count += np.array([0, 0, 0, 3, 2, 1, 0, 0])
        print(count)
    q22 = st.checkbox('疲労時や夜によく手のひらや足の裏が熱くなる')
    if q22:
        count += np.array([0, 0, 0, 3, 0, 0, 0, 0])
        print(count)
    submit_btn = st.form_submit_button('送信')
    if submit_btn:
        a = np.round(count[0]/2)
        b = np.round(count[1]/2)
        c = np.round(count[2]/2)
        d = np.round(count[3]/2)
        e = np.round(count[4]/2)
        f = np.round(count[5]/2)
        g = np.round(count[6]/2)
        h = np.round(count[7]/2)

        print(a+b+c+d)
        # レーダーチャート表示
        values = count
        labels = ['脾虚', '腎陽虚', '血虚', '陰虚', '気滞', '湿熱', '血瘀', '湿痰']

        # 多角形を閉じるためにデータの最後に最初の値を追加する。
        radar_values = np.concatenate([values, [values[0]]])
        # プロットする角度を生成する。
        angles = np.linspace(0, 2 * np.pi, len(labels) + 1, endpoint=True)
        # メモリ軸の生成
        rgrids = [0, 2, 4, 6, 8, 10]

        fig = plt.figure(facecolor="w")
        # 極座標でaxを作成
        ax = fig.add_subplot(1, 1, 1, polar=True)
        # レーダーチャートの線を引く
        ax.plot(angles, radar_values)
        # 　レーダーチャートの内側を塗りつぶす
        ax.fill(angles, radar_values, alpha=0.2)
        # 項目ラベルの表示
        ax.set_thetagrids(angles[:-1] * 180 / np.pi, labels)
        # 円形の目盛線を消す
        ax.set_rgrids([])
        # 一番外側の円を消す
        ax.spines['polar'].set_visible(False)
        # 始点を上(北)に変更
        ax.set_theta_zero_location("N")
        # 時計回りに変更(デフォルトの逆回り)
        ax.set_theta_direction(-1)

        # 多角形の目盛線を引く
        for grid_value in rgrids:
            grid_values = [grid_value] * (len(labels) + 1)
            ax.plot(angles, grid_values, color="gray", linewidth=0.5)

        # メモリの値を表示する
        for t in rgrids:
            # xが偏角、yが絶対値でテキストの表示場所が指定される
            ax.text(x=0, y=t, s=t)

        # rの範囲を指定
        ax.set_rlim([min(rgrids), max(rgrids)])

        # ax.set_title("判定結果", pad=20)
        # plt.show()
        plt.savefig('result.jpg')
        st.success('診断結果を保存しました', icon="✅")
open_btn = st.button('分析チャートを開く')
image = Image.open('result.jpg')
if open_btn:
    st.image(image)

    expand_a = st.expander("脾虚の説明")
    expand_a.write("""
    胃腸が弱く疲れやすい体質。
    脾虚は消化機能を担い、気・血・津液を生成する役割を持つ脾の作用が低下している状態。
    飲食物からエネルギーを取り出す力が弱く気が不足気味。
    この為、疲れやすい、風邪を引きやすいといった傾向が見られる。
    体質改善には食べ過ぎ、冷たい飲食物の摂りすぎに注意
    """)
    expand_b = st.expander("腎陽虚の説明")
    expand_b.write("""
    熱不足で冷えが強い体質。腎陽は腎に蓄えられている熱源のこと。腎陽虚はこの熱源が不足し冷えが強い体質のこと。
    むくみ、冷え、頻尿に影響があり体を冷やさないように注意し気を消耗しすぎないよう十分な休息が重要となる
    """)
    expand_c = st.expander("血虚の説明")
    expand_c.write("""
    女性に多い血が不足した体質。全身に栄養を届けるのが血であり血虚とはこの血が不足した状態。血虚は皮膚の乾燥、
    筋肉の疲れ、引きつり、手足の痺れ、冷えなどを引き起こしやすくなる。体質の改善のため血の元となる人参、ほうれん草、
    ひじきなどの食材をしっかり摂り、十分な睡眠を心がける
    """)
    expand_d = st.expander("陰虚の説明")
    expand_d.write("""
    津液の不足で乾燥気味の体質。陰とは体を潤す津液のことであり陰虚とは津液が不足した状態のこと。体内の水分が不足すると
    相対的に熱が強くなる為、皮膚や髪が乾燥気味だったり熱がないのに熱っぽく感じたりといった傾向が見られる。
    過労や睡眠不足、ストレスなどは津液を過剰に消耗するため陰虚を引き起こす原因となりやすい。
    体質改善には過労を控え、十分な睡眠を心がける
    """)
    expand_e = st.expander("気滞の説明")
    expand_e.write("""
    気の滞りでイライラしがちな体質。気の循環が滞っている状態が気滞で部分的に過剰、不足が起きており
    元気なようで疲れやすい、顔は火照るのに手足は冷たいといった症状がある。ゲップやおならが多いのも
    気滞の１つでストレスや抑うつ感、考え事、心配事が原因になりやすいのでリラックスが必要
    """)
    expand_f = st.expander("湿熱の説明")
    expand_f.write("""
    余分な津液と熱がこもった体質。過剰な津液が病的な熱と結びつくとドロドロとした状態になる。
    このドロドロが体内に溜まった体質を湿熱といい、暑がりで汗っかき、体格ががっちりしているといった
    特徴がある。ドロドロしたものは熱を帯びた状態で１カ所に滞るため、かゆみや腫れ、吹き出物、化膿などを
    引き起こす。体質改善の為には、湿熱の元となる甘いものや辛いもの、脂っこいものなどを控えることが大切
    """)
    expand_g = st.expander("血瘀の説明")
    expand_g.write("""
    皮膚が黒っぽい、血が滞った体質。血の巡りが滞っている体質を血瘀という。血が滞ると黒っぽくみえ、肌の色が
    浅黒くツヤがないといった傾向が見られる。血の巡りが悪いと冷えが生じやすいほか、肩こりや頭痛、月経痛なども
    現れる。血瘀を招く主な原因には血の巡りを先導する気が不足しているか滞っていることが挙げられる。
    体質改善には気の滞りの原因となるストレスを解消するのが有効
    """)
    expand_h = st.expander("湿痰の説明")
    expand_h.write("""
    津液が過剰な水太り体質。津液が過剰に溜まると湿となり、さらに湿が固まって動きが悪くなると痰となる。
    この湿や痰が体内に溜まっている体質を湿痰と呼ぶ。湿痰は体中に水袋を抱えているような状態なので、気温に
    左右されやすく、寒がりで暑がりの傾向がある。水太りの人にこのタイプが多く色白で疲れやすい特徴もある。
    体質改善をするには水分の摂りすぎを改め、適度な運動を取り入れるのが有効
    """)