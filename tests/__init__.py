from phi_utils.edit.saves import complete_song_list,update_song_list_difficulty
from phi_utils.models.saves import GameSaves, GameKey, GameKeyItem, SingleScore
from phi_utils.models.difficulty import Difficulty,SingleDifficulty
from phi_utils.models.info import SingleSongINFO, SongINFO

# 测试key列表
test_game_key_list = GameKey(key_list=[GameKeyItem(id="test",type=[True,False],flag=[False,True])])

# 测试打歌列表
test_song_list = [SingleScore(
    score=1000000,
    acc=99.5,
    fc=True,
    id="test",
    name="测试单",
    difficulty=11.45,
    level="EZ"
)]

# 测试定数列表
difficulty_list = Difficulty(list=[
    SingleDifficulty(
        id="test",
        list=[
            {"EZ":15.5},
            {"HD":11.4}
            ]
    )])

song_info = SongINFO(list=[
    SingleSongINFO(
        id="test",
        name="测试单曲",
        composer="千柒",
        illustrator="废酱",
        chart=[
            {"EZ":"我"},
            {"HD":"烧饼"},
            {"IN":"文酱"},
        ]
    )])

# 获得存档
test_game_saves = GameSaves(game_key=test_game_key_list,song_list=test_song_list)

# 补全存档
complete_test_game_saves = complete_song_list(game_saves=test_game_saves,difficultys=difficulty_list,song_info=song_info)

# 输出
print(complete_test_game_saves.model_dump_json())
print(complete_test_game_saves.song_list[0].rks)

# 更新存档定数
update_difficulty_game_saves = update_song_list_difficulty(game_saves=complete_test_game_saves,difficultys=difficulty_list)

# 输出
print(update_difficulty_game_saves.model_dump_json())
print(update_difficulty_game_saves.song_list[0].rks)