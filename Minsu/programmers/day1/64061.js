// 2019 카카오 개발자 겨울 인턴쉽

function solution(board, moves) {
  let answer = 0,
    arr = [],
    blen = board.length; // board 길이

  // moves의 전체 길이를 이용하여 for 문을 돌린다.
  for (let i = 0; i < moves.length; i++) {
    let j = 0,
      m = moves[i] - 1, // ?
      alen = arr.length; // 바구니의 길이

    //
    while (j < blen && board[j][m] == 0) j++;

    if (j == blen) continue;

    arr.push(board[j][m]);

    board[j][m] = 0;

    if (alen != 0 && arr[alen] == arr[alen - 1]) {
      arr.splice(alen - 1, 2);
      answer += 2;
    }
  }
  return answer;
}
