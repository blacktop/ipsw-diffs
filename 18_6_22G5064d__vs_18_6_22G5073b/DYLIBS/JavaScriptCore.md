## JavaScriptCore

> `/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore`

```diff

-621.3.7.10.1
-  __TEXT.__text: 0x17231b0
+621.3.8.0.0
+  __TEXT.__text: 0x1723184
   __TEXT.__jsc_int: 0x7e260
   __TEXT.__auth_stubs: 0x2d90
   __TEXT.__objc_methlist: 0xb9c

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 24373980-AD48-325D-9384-172C1FBB29CD
-  Functions: 43447
-  Symbols:   87872
+  UUID: A42D94F8-6B79-3C0A-920A-64F0F2992F5F
+  Functions: 43445
+  Symbols:   87868
   CStrings:  19925
 
Symbols:
- __ZN3JSC4Yarr22YarrPatternConstructor8copyTermERNS0_11PatternTermEb
- __ZN3WTF6VectorIN3JSC4Yarr22YarrPatternConstructor26UnresolvedForwardReferenceELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEE10removeLastEv
Functions (modified):
~ __ZN3JSC4Yarr22YarrPatternConstructor12quantifyAtomEjjb : 1060 -> 1428
~ _llint_slow_path_get_by_val : 9436 -> 9432

Functions (removed):
- __ZN3JSC4Yarr22YarrPatternConstructor8copyTermERNS0_11PatternTermEb
- _pas_reallocation_did_fail
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~B4tVugARAMP8QKfw-oExyoEidJr5Aaoej6HOqy8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/Assertions.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tVugARAMP8QKfw-oExyoEidJr5Aaoej6HOqy8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tVugARAMP8QKfw-oExyoEidJr5Aaoej6HOqy8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/Deque.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tVugARAMP8QKfw-oExyoEidJr5Aaoej6HOqy8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/Dominators.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tVugARAMP8QKfw-oExyoEidJr5Aaoej6HOqy8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/FastBitVector.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tVugARAMP8QKfw-oExyoEidJr5Aaoej6HOqy8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/HashTable.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tVugARAMP8QKfw-oExyoEidJr5Aaoej6HOqy8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/IndexMap.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tVugARAMP8QKfw-oExyoEidJr5Aaoej6HOqy8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/JSONValues.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tVugARAMP8QKfw-oExyoEidJr5Aaoej6HOqy8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/LazyRef.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tVugARAMP8QKfw-oExyoEidJr5Aaoej6HOqy8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/LazyUniqueRef.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tVugARAMP8QKfw-oExyoEidJr5Aaoej6HOqy8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/Liveness.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tVugARAMP8QKfw-oExyoEidJr5Aaoej6HOqy8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/LockAlgorithmInlines.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tVugARAMP8QKfw-oExyoEidJr5Aaoej6HOqy8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/MallocSpan.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tVugARAMP8QKfw-oExyoEidJr5Aaoej6HOqy8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/Markable.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tVugARAMP8QKfw-oExyoEidJr5Aaoej6HOqy8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/NaturalLoops.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tVugARAMP8QKfw-oExyoEidJr5Aaoej6HOqy8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/RedBlackTree.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tVugARAMP8QKfw-oExyoEidJr5Aaoej6HOqy8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/RefCounted.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tVugARAMP8QKfw-oExyoEidJr5Aaoej6HOqy8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/SinglyLinkedListWithTail.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tVugARAMP8QKfw-oExyoEidJr5Aaoej6HOqy8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tVugARAMP8QKfw-oExyoEidJr5Aaoej6HOqy8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tVugARAMP8QKfw-oExyoEidJr5Aaoej6HOqy8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tVugARAMP8QKfw-oExyoEidJr5Aaoej6HOqy8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/TrailingArray.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tVugARAMP8QKfw-oExyoEidJr5Aaoej6HOqy8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/WeakPtr.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tVugARAMP8QKfw-oExyoEidJr5Aaoej6HOqy8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tVugARAMP8QKfw-oExyoEidJr5Aaoej6HOqy8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
+ "/AppleInternal/Library/BuildRoots/4~B4tVugARAMP8QKfw-oExyoEidJr5Aaoej6HOqy8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
- "/AppleInternal/Library/BuildRoots/4~B31tugBgFPguJVAFumRuY69Ge8MyE7ysHdbrodc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/Assertions.h"
- "/AppleInternal/Library/BuildRoots/4~B31tugBgFPguJVAFumRuY69Ge8MyE7ysHdbrodc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
- "/AppleInternal/Library/BuildRoots/4~B31tugBgFPguJVAFumRuY69Ge8MyE7ysHdbrodc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/Deque.h"
- "/AppleInternal/Library/BuildRoots/4~B31tugBgFPguJVAFumRuY69Ge8MyE7ysHdbrodc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/Dominators.h"
- "/AppleInternal/Library/BuildRoots/4~B31tugBgFPguJVAFumRuY69Ge8MyE7ysHdbrodc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/FastBitVector.h"
- "/AppleInternal/Library/BuildRoots/4~B31tugBgFPguJVAFumRuY69Ge8MyE7ysHdbrodc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/HashTable.h"
- "/AppleInternal/Library/BuildRoots/4~B31tugBgFPguJVAFumRuY69Ge8MyE7ysHdbrodc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/IndexMap.h"
- "/AppleInternal/Library/BuildRoots/4~B31tugBgFPguJVAFumRuY69Ge8MyE7ysHdbrodc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/JSONValues.h"
- "/AppleInternal/Library/BuildRoots/4~B31tugBgFPguJVAFumRuY69Ge8MyE7ysHdbrodc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/LazyRef.h"
- "/AppleInternal/Library/BuildRoots/4~B31tugBgFPguJVAFumRuY69Ge8MyE7ysHdbrodc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/LazyUniqueRef.h"
- "/AppleInternal/Library/BuildRoots/4~B31tugBgFPguJVAFumRuY69Ge8MyE7ysHdbrodc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/Liveness.h"
- "/AppleInternal/Library/BuildRoots/4~B31tugBgFPguJVAFumRuY69Ge8MyE7ysHdbrodc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/LockAlgorithmInlines.h"
- "/AppleInternal/Library/BuildRoots/4~B31tugBgFPguJVAFumRuY69Ge8MyE7ysHdbrodc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/MallocSpan.h"
- "/AppleInternal/Library/BuildRoots/4~B31tugBgFPguJVAFumRuY69Ge8MyE7ysHdbrodc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/Markable.h"
- "/AppleInternal/Library/BuildRoots/4~B31tugBgFPguJVAFumRuY69Ge8MyE7ysHdbrodc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/NaturalLoops.h"
- "/AppleInternal/Library/BuildRoots/4~B31tugBgFPguJVAFumRuY69Ge8MyE7ysHdbrodc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/RedBlackTree.h"
- "/AppleInternal/Library/BuildRoots/4~B31tugBgFPguJVAFumRuY69Ge8MyE7ysHdbrodc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/RefCounted.h"
- "/AppleInternal/Library/BuildRoots/4~B31tugBgFPguJVAFumRuY69Ge8MyE7ysHdbrodc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/SinglyLinkedListWithTail.h"
- "/AppleInternal/Library/BuildRoots/4~B31tugBgFPguJVAFumRuY69Ge8MyE7ysHdbrodc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "/AppleInternal/Library/BuildRoots/4~B31tugBgFPguJVAFumRuY69Ge8MyE7ysHdbrodc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
- "/AppleInternal/Library/BuildRoots/4~B31tugBgFPguJVAFumRuY69Ge8MyE7ysHdbrodc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
- "/AppleInternal/Library/BuildRoots/4~B31tugBgFPguJVAFumRuY69Ge8MyE7ysHdbrodc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/TrailingArray.h"
- "/AppleInternal/Library/BuildRoots/4~B31tugBgFPguJVAFumRuY69Ge8MyE7ysHdbrodc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/WeakPtr.h"
- "/AppleInternal/Library/BuildRoots/4~B31tugBgFPguJVAFumRuY69Ge8MyE7ysHdbrodc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
- "/AppleInternal/Library/BuildRoots/4~B31tugBgFPguJVAFumRuY69Ge8MyE7ysHdbrodc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
- "/AppleInternal/Library/BuildRoots/4~B31tugBgFPguJVAFumRuY69Ge8MyE7ysHdbrodc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.6.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"

```
