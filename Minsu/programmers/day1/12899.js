// 124 나라의 숫자

function solution(n) {
  var answer = "";
  var mod; // 나머지

  while (n) {
    mod = n % 3; // 0, 1, 2 중에 나머지가 나온다.
    n = parseInt(n / 3); // 몫을 정수로 표현하여, 0, 1, 2 만 나오게 한다.

    if (mod == 0) {
      // 1,2,4 니라 이므로, 나누어 떨어지는 경우는 3의 배수일 경우에 4로 대체한다.
      n -= 1; // 그리고 몫 부분에 1을 뺀다.
      answer += "4";
    } else answer += mod;
  }
  return answer.split("").reverse().join(""); // 문자열 처리
}
