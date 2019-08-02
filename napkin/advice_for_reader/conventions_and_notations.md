# 6 Convenvtions and notations

## 6.1 Sets and equivalence relations

- 동치관계
  - `~` : 집합 X에 대한 동치, 재귀, transitive
  - 동치 관계는 집합 X를 여러 동치 클래스로 분할한다.
    - X~A~B 관계에 있는 것을 X/~ 라고 한다.
    - 동치 클래스 요소는 동치 클래스를 대표한다.

- ≅
  - reasonable category에 있는 isomorphism 관계에 있을 때 사용한다.
  - = 를 _ 로 표기하는 책도 있지만 Napkin에서는 = 를 사용하겠다.
    - _ 로 표기할 때는 homotopic paths에 사용하겠다.

- 부분집합
  - a ⊂ b 이면서 a = b일 때 ⊆ 를 사용한다. 
    - ⊂ 는 모호한 표현이다.
      - 동치가 확실히 유지되지 않는 드문 상황에 사용하겠다. 
  
  - 진부분집합
    - a ⊂ b 이면서 a != b일 때 ⊊ 를 사용한다. 

- 차집합
  - S \ T는 S - T를 의미한다.

- 멱집합 (The power set of S (i.e., the set of subsets of S))
  - 표기는 2 ^ S 또는 P(S)로 한다.
    - 왜 2의 거듭제곱꼴로 나타내는가는 부분집합의 개수와 연관되어 있을 것이라고 추정한다.

## 6.2 Functions

- 원상(pre-image)
  - 상이 맵핑되기 전 상태의 원래의 상

   ```
   # f는 원상 
   f(T) := {x ∈ X| f(x) ∈ T}

   # python code
   {x for x in X in f(x) ∈ T}
   ```

- 상 (image)
  - 상은 함수 공역의 서브셋이며, 함수의 서브셋에서 나오는 함수의 출력이다. [출처](https://en.wikipedia.org/wiki/Image_(mathematics))

  ```
  # f 는 상
  f(S) := {f(x)| x ∈ S}

  # python code 
  {f(x) for x in S}
  ```
  - abuse of notation
    - f[s]나 f"(S) 등으로 쓰는 사람도 있지만 napkin에서는 다른 표기를 하겠음.

- restriction
  - S ⊆ X 일 때 S에 대한 함수 f를 제한하는 경우에, 별도의 표기를 한다. 
  - [참고](https://en.wikipedia.org/wiki/Restriction_(mathematics)

- injective function(단사함수), surjective function(전사함수)
  - 통틀어서 표기할 수 있다. 
  - 단사함수 : [참고](https://en.wikipedia.org/wiki/Injective_function) 
  - 전사함수 : [참고](https://en.wikipedia.org/wiki/Surjective_function) 
