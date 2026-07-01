## CoreMotionAlgorithms

> `/System/Library/PrivateFrameworks/CoreMotionAlgorithms.framework/CoreMotionAlgorithms`

```diff
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__oslogstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
CStrings:
+ "Assertion failed: (fIirFilterParams != __null) && (fIirFilterParams->filterOrder <= kMaxFilterOrder), file /Library/Caches/com.apple.xbs/06262DB4-FF2A-4C05-B195-1CD6B7C27F33/TemporaryDirectory.0bNcTi/Sources/CoreMotionAlgorithmsFramework/Oscar/CMIirFilter.cpp, line 17,IirFilterParams,%p,filterOrder,%d,maxFilterOrder,%d."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/06262DB4-FF2A-4C05-B195-1CD6B7C27F33/TemporaryDirectory.0bNcTi/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 231,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/06262DB4-FF2A-4C05-B195-1CD6B7C27F33/TemporaryDirectory.0bNcTi/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 237,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/06262DB4-FF2A-4C05-B195-1CD6B7C27F33/TemporaryDirectory.0bNcTi/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 71,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/06262DB4-FF2A-4C05-B195-1CD6B7C27F33/TemporaryDirectory.0bNcTi/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 78,invalid col %zu > %zu."
+ "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/06262DB4-FF2A-4C05-B195-1CD6B7C27F33/TemporaryDirectory.0bNcTi/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 232,invalid element %zu <= %zu."
+ "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/06262DB4-FF2A-4C05-B195-1CD6B7C27F33/TemporaryDirectory.0bNcTi/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 238,invalid element %zu <= %zu."
+ "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/06262DB4-FF2A-4C05-B195-1CD6B7C27F33/TemporaryDirectory.0bNcTi/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMVector.h, line 273,invalid index %zu >= %zu."
+ "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/06262DB4-FF2A-4C05-B195-1CD6B7C27F33/TemporaryDirectory.0bNcTi/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMVector.h, line 279,invalid index %zu >= %zu."
+ "Assertion failed: i < fCapacity, file /Library/Caches/com.apple.xbs/06262DB4-FF2A-4C05-B195-1CD6B7C27F33/TemporaryDirectory.0bNcTi/Sources/CoreMotionAlgorithmsFramework/Oscar/CMQueue.h, line 233,i,%zu,capacity,%u."
+ "Assertion failed: i0 < N-Ni+1 && j0 < N-Nj+1, file /Library/Caches/com.apple.xbs/06262DB4-FF2A-4C05-B195-1CD6B7C27F33/TemporaryDirectory.0bNcTi/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 302,indices exceed factored matrix size."
+ "Assertion failed: ldx < M*N, file /Library/Caches/com.apple.xbs/06262DB4-FF2A-4C05-B195-1CD6B7C27F33/TemporaryDirectory.0bNcTi/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 84,invalid element %zu >= %zu."
+ "Assertion failed: rhs.capacity() == capacity(), file /Library/Caches/com.apple.xbs/06262DB4-FF2A-4C05-B195-1CD6B7C27F33/TemporaryDirectory.0bNcTi/Sources/CoreMotionAlgorithmsFramework/Oscar/CMQueue.h, line 70,capacity,%zu,%zu."
+ "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/06262DB4-FF2A-4C05-B195-1CD6B7C27F33/TemporaryDirectory.0bNcTi/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 70,invalid row %zu > %zu."
+ "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/06262DB4-FF2A-4C05-B195-1CD6B7C27F33/TemporaryDirectory.0bNcTi/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 77,invalid row %zu > %zu."
+ "Assertion failed: row < N, file /Library/Caches/com.apple.xbs/06262DB4-FF2A-4C05-B195-1CD6B7C27F33/TemporaryDirectory.0bNcTi/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 186,invalid row %zu > %zu."
+ "Assertion failed: row < N, file /Library/Caches/com.apple.xbs/06262DB4-FF2A-4C05-B195-1CD6B7C27F33/TemporaryDirectory.0bNcTi/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 191,invalid row %zu > %zu."
- "Assertion failed: (fIirFilterParams != __null) && (fIirFilterParams->filterOrder <= kMaxFilterOrder), file /Library/Caches/com.apple.xbs/3A7E4A9D-F3ED-4BD4-AD45-B45F8DDCDDE6/TemporaryDirectory.FSRS49/Sources/CoreMotionAlgorithmsFramework/Oscar/CMIirFilter.cpp, line 17,IirFilterParams,%p,filterOrder,%d,maxFilterOrder,%d."
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/3A7E4A9D-F3ED-4BD4-AD45-B45F8DDCDDE6/TemporaryDirectory.FSRS49/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 231,invalid col %zu > %zu."
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/3A7E4A9D-F3ED-4BD4-AD45-B45F8DDCDDE6/TemporaryDirectory.FSRS49/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 237,invalid col %zu > %zu."
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/3A7E4A9D-F3ED-4BD4-AD45-B45F8DDCDDE6/TemporaryDirectory.FSRS49/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 71,invalid col %zu > %zu."
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/3A7E4A9D-F3ED-4BD4-AD45-B45F8DDCDDE6/TemporaryDirectory.FSRS49/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 78,invalid col %zu > %zu."
- "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/3A7E4A9D-F3ED-4BD4-AD45-B45F8DDCDDE6/TemporaryDirectory.FSRS49/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 232,invalid element %zu <= %zu."
- "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/3A7E4A9D-F3ED-4BD4-AD45-B45F8DDCDDE6/TemporaryDirectory.FSRS49/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 238,invalid element %zu <= %zu."
- "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/3A7E4A9D-F3ED-4BD4-AD45-B45F8DDCDDE6/TemporaryDirectory.FSRS49/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMVector.h, line 273,invalid index %zu >= %zu."
- "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/3A7E4A9D-F3ED-4BD4-AD45-B45F8DDCDDE6/TemporaryDirectory.FSRS49/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMVector.h, line 279,invalid index %zu >= %zu."
- "Assertion failed: i < fCapacity, file /Library/Caches/com.apple.xbs/3A7E4A9D-F3ED-4BD4-AD45-B45F8DDCDDE6/TemporaryDirectory.FSRS49/Sources/CoreMotionAlgorithmsFramework/Oscar/CMQueue.h, line 233,i,%zu,capacity,%u."
- "Assertion failed: i0 < N-Ni+1 && j0 < N-Nj+1, file /Library/Caches/com.apple.xbs/3A7E4A9D-F3ED-4BD4-AD45-B45F8DDCDDE6/TemporaryDirectory.FSRS49/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 302,indices exceed factored matrix size."
- "Assertion failed: ldx < M*N, file /Library/Caches/com.apple.xbs/3A7E4A9D-F3ED-4BD4-AD45-B45F8DDCDDE6/TemporaryDirectory.FSRS49/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 84,invalid element %zu >= %zu."
- "Assertion failed: rhs.capacity() == capacity(), file /Library/Caches/com.apple.xbs/3A7E4A9D-F3ED-4BD4-AD45-B45F8DDCDDE6/TemporaryDirectory.FSRS49/Sources/CoreMotionAlgorithmsFramework/Oscar/CMQueue.h, line 70,capacity,%zu,%zu."
- "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/3A7E4A9D-F3ED-4BD4-AD45-B45F8DDCDDE6/TemporaryDirectory.FSRS49/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 70,invalid row %zu > %zu."
- "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/3A7E4A9D-F3ED-4BD4-AD45-B45F8DDCDDE6/TemporaryDirectory.FSRS49/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 77,invalid row %zu > %zu."
- "Assertion failed: row < N, file /Library/Caches/com.apple.xbs/3A7E4A9D-F3ED-4BD4-AD45-B45F8DDCDDE6/TemporaryDirectory.FSRS49/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 186,invalid row %zu > %zu."
- "Assertion failed: row < N, file /Library/Caches/com.apple.xbs/3A7E4A9D-F3ED-4BD4-AD45-B45F8DDCDDE6/TemporaryDirectory.FSRS49/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 191,invalid row %zu > %zu."

```
