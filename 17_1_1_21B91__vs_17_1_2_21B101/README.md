# 17.1.1 (21B91) .vs 17.1.2 (21B101)

## IPSWs

- `iPhone16,1_17.1.1_21B91_Restore.ipsw`
- `iPhone16,1_17.1.2_21B101_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 17.1.1 *(21B91)* | 23.1.0 | 10002.42.9~2 | Tue, 10Oct2023 02:21:19 PDT |
| 17.1.2 *(21B101)* | 23.1.0 | 10002.42.9~2 | Tue, 10Oct2023 02:21:19 PDT |

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 17.1.1 *(21B91)* | 616.2.9.10.11 |
| 17.1.2 *(21B101)* | 616.2.9.10.13 |

### Dylibs

#### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### JavaScriptCore

>  `/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore`

```diff

-616.2.9.10.11
-  __TEXT.__text: 0x15bf060
+616.2.9.10.13
+  __TEXT.__text: 0x15bf3c4
   __TEXT.__auth_stubs: 0x2bb0
   __TEXT.__objc_methlist: 0x950
   __TEXT.__const: 0x7d138
-  __TEXT.__cstring: 0xb6731
+  __TEXT.__cstring: 0xb679c
   __TEXT.__gcc_except_tab: 0x1d14
   __TEXT.__oslogstring: 0x41e
   __TEXT.__unwind_info: 0x1e64

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 36013
-  Symbols:   71919
-  CStrings:  18362
+  Functions: 36011
+  Symbols:   71915
+  CStrings:  18365
 
Symbols:
- __ZN3JSC9Structure12setMaxOffsetERNS_2VMEi
- __ZN3WTF6VectorIN3JSC7JSValueELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEEC1Em
CStrings:
+ "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__algorithm/clamp.h"
+ "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__algorithm/pop_heap.h"
+ "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__algorithm/sift_down.h"
+ "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h"
+ "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__string/char_traits.h"
+ "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__tree"
+ "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__utility/unreachable.h"
+ "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/array"
+ "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/optional"
+ "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/span"
+ "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/string"
+ "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/Assertions.h"
+ "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
+ "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/Deque.h"
+ "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/IndexMap.h"
+ "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/Liveness.h"
+ "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/LockAlgorithmInlines.h"
+ "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/NaturalLoops.h"
+ "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
+ "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/RedBlackTree.h"
+ "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/SinglyLinkedListWithTail.h"
+ "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
+ "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
+ "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
+ "/AppleInternal/Library/BuildRoots/f0852955-8592-11ee-af62-2a65a1af8551/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
+ "inst.args[2].asTrustedImm32().m_value < 32"
+ "inst.args[2].asTrustedImm32().m_value < 64"
+ "inst.args[2].isImm()"
- "/AppleInternal/Library/BuildRoots/2f527c0a-7035-11ee-8acd-aa4f15650fdf/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__algorithm/clamp.h"
- "/AppleInternal/Library/BuildRoots/2f527c0a-7035-11ee-8acd-aa4f15650fdf/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__algorithm/pop_heap.h"
- "/AppleInternal/Library/BuildRoots/2f527c0a-7035-11ee-8acd-aa4f15650fdf/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__algorithm/sift_down.h"
- "/AppleInternal/Library/BuildRoots/2f527c0a-7035-11ee-8acd-aa4f15650fdf/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h"
- "/AppleInternal/Library/BuildRoots/2f527c0a-7035-11ee-8acd-aa4f15650fdf/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__string/char_traits.h"
- "/AppleInternal/Library/BuildRoots/2f527c0a-7035-11ee-8acd-aa4f15650fdf/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__tree"
- "/AppleInternal/Library/BuildRoots/2f527c0a-7035-11ee-8acd-aa4f15650fdf/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/__utility/unreachable.h"
- "/AppleInternal/Library/BuildRoots/2f527c0a-7035-11ee-8acd-aa4f15650fdf/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/array"
- "/AppleInternal/Library/BuildRoots/2f527c0a-7035-11ee-8acd-aa4f15650fdf/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/optional"
- "/AppleInternal/Library/BuildRoots/2f527c0a-7035-11ee-8acd-aa4f15650fdf/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/span"
- "/AppleInternal/Library/BuildRoots/2f527c0a-7035-11ee-8acd-aa4f15650fdf/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/include/c++/v1/string"
- "/AppleInternal/Library/BuildRoots/2f527c0a-7035-11ee-8acd-aa4f15650fdf/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/Assertions.h"
- "/AppleInternal/Library/BuildRoots/2f527c0a-7035-11ee-8acd-aa4f15650fdf/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
- "/AppleInternal/Library/BuildRoots/2f527c0a-7035-11ee-8acd-aa4f15650fdf/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/Deque.h"
- "/AppleInternal/Library/BuildRoots/2f527c0a-7035-11ee-8acd-aa4f15650fdf/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/IndexMap.h"
- "/AppleInternal/Library/BuildRoots/2f527c0a-7035-11ee-8acd-aa4f15650fdf/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/Liveness.h"
- "/AppleInternal/Library/BuildRoots/2f527c0a-7035-11ee-8acd-aa4f15650fdf/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/LockAlgorithmInlines.h"
- "/AppleInternal/Library/BuildRoots/2f527c0a-7035-11ee-8acd-aa4f15650fdf/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/NaturalLoops.h"
- "/AppleInternal/Library/BuildRoots/2f527c0a-7035-11ee-8acd-aa4f15650fdf/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
- "/AppleInternal/Library/BuildRoots/2f527c0a-7035-11ee-8acd-aa4f15650fdf/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/RedBlackTree.h"
- "/AppleInternal/Library/BuildRoots/2f527c0a-7035-11ee-8acd-aa4f15650fdf/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/SinglyLinkedListWithTail.h"
- "/AppleInternal/Library/BuildRoots/2f527c0a-7035-11ee-8acd-aa4f15650fdf/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "/AppleInternal/Library/BuildRoots/2f527c0a-7035-11ee-8acd-aa4f15650fdf/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
- "/AppleInternal/Library/BuildRoots/2f527c0a-7035-11ee-8acd-aa4f15650fdf/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
- "/AppleInternal/Library/BuildRoots/2f527c0a-7035-11ee-8acd-aa4f15650fdf/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
- "/AppleInternal/Library/BuildRoots/2f527c0a-7035-11ee-8acd-aa4f15650fdf/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"

```


</details>

## EOF
