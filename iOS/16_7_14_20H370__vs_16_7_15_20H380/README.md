# 16.7.14 (20H370) .vs 16.7.15 (20H380)

## IPSWs

- `iPhone10,3,iPhone10,6_16.7.14_20H370_Restore.ipsw`
- `iPhone10,3,iPhone10,6_16.7.15_20H380_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 16.7.14 *(20H370)* | 22.6.0 | 8796.142.1.703.8~1 | Tue, 02Jul2024 20:47:35 PDT |
| 16.7.15 *(20H380)* | 22.6.0 | 8796.142.1.703.8~1 | Tue, 02Jul2024 20:47:35 PDT |

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 16.7.14 *(20H370)* | 615.8.1.10.2 |
| 16.7.15 *(20H380)* | 615.8.1.10.3 |

### Dylibs

#### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### JavaScriptCore

>  `/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore`

```diff

-615.8.1.10.2
-  __TEXT.__text: 0x13b087c
+615.8.1.10.3
+  __TEXT.__text: 0x13b09b8
   __TEXT.__stubs: 0x20ac
   __TEXT.__objc_methlist: 0x908
-  __TEXT.__const: 0x75160
-  __TEXT.__cstring: 0xb83ca
+  __TEXT.__const: 0x75140
+  __TEXT.__cstring: 0xb85ee
   __TEXT.__gcc_except_tab: 0x1b3c
   __TEXT.__oslogstring: 0x82f
   __TEXT.__unwind_info: 0x1af0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 13678881-62EB-3DD7-ACF0-246B60F80549
-  Functions: 33121
-  Symbols:   66417
-  CStrings:  17807
+  UUID: 8697D573-7AFD-3BBE-BBEB-C45817C0CB1E
+  Functions: 33106
+  Symbols:   66381
+  CStrings:  17814
 
Symbols:
+ __ZNK3JSC4Wasm13SectionParser4failIJPKcjS4_S4_EEENSt12experimental15fundamentals_v310unexpectedIN3WTF6StringEEEDpT_
- __ZN3JSC4Wasm13SectionParser16parseElementKindERh
- __ZN3JSC4Wasm13SectionParser19parseRecursionGroupEjRN3WTF6RefPtrINS0_14TypeDefinitionENS2_12RawPtrTraitsIS4_EENS2_21DefaultRefDerefTraitsIS4_EEEE
- __ZN3JSC4Wasm13SectionParser20checkSubtypeValidityERKNS0_14TypeDefinitionES4_
- __ZN3JSC4Wasm15TypeInformation31typeDefinitionForRecursionGroupERKN3WTF6VectorImLm0ENS2_15CrashOnOverflowELm16ENS2_10FastMallocEEE
- __ZN3JSC4Wasm17ModuleInformation19addDeclaredFunctionEj
- __ZN3JSC4Wasm17ModuleInformation20addDeclaredExceptionEj
- __ZN3JSC4Wasm6ExportC1EOS1_
- __ZN3JSC4Wasm6ImportC1EOS1_
- __ZN3WTF11VectorMoverILb0EN3JSC4Wasm12FunctionDataEE4moveEPS3_S5_S5_
- __ZN3WTF11VectorMoverILb0EN3JSC4Wasm6ExportEE4moveEPS3_S5_S5_
- __ZN3WTF11VectorMoverILb0EN3JSC4Wasm6ImportEE4moveEPS3_S5_S5_
- __ZN3WTF11VectorMoverILb0EN3JSC4Wasm7ElementEE4moveEPS3_S5_S5_
- __ZN3WTF16VectorBufferBaseIjNS_10FastMallocEE14allocateBufferILNS_13FailureActionE1EEEbm
- __ZN3WTF6VectorIN3JSC4Wasm12FunctionDataELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEE15reserveCapacityILNS_13FailureActionE1EEEbm
- __ZN3WTF6VectorIN3JSC4Wasm6ExportELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEE15reserveCapacityILNS_13FailureActionE1EEEbm
- __ZN3WTF6VectorIN3JSC4Wasm6ImportELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEE15reserveCapacityILNS_13FailureActionE1EEEbm
- __ZN3WTF6VectorIN3JSC4Wasm7ElementELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEE15reserveCapacityILNS_13FailureActionE1EEEbm
- __ZN3WTF6VectorINSt3__110unique_ptrIN3JSC4Wasm7SegmentEPFvPS5_EEELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEE15reserveCapacityILNS_13FailureActionE1EEEbm
- __ZN3WTF6VectorIjLm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEE15reserveCapacityILNS_13FailureActionE1EEEbm
CStrings:
+ " type "
+ "/AppleInternal/Library/BuildRoots/f8a064a4-fd32-11f0-9fbf-467786e86c71/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/Assertions.h"
+ "/AppleInternal/Library/BuildRoots/f8a064a4-fd32-11f0-9fbf-467786e86c71/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
+ "/AppleInternal/Library/BuildRoots/f8a064a4-fd32-11f0-9fbf-467786e86c71/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/Deque.h"
+ "/AppleInternal/Library/BuildRoots/f8a064a4-fd32-11f0-9fbf-467786e86c71/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/IndexMap.h"
+ "/AppleInternal/Library/BuildRoots/f8a064a4-fd32-11f0-9fbf-467786e86c71/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/Liveness.h"
+ "/AppleInternal/Library/BuildRoots/f8a064a4-fd32-11f0-9fbf-467786e86c71/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/LockAlgorithmInlines.h"
+ "/AppleInternal/Library/BuildRoots/f8a064a4-fd32-11f0-9fbf-467786e86c71/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/NaturalLoops.h"
+ "/AppleInternal/Library/BuildRoots/f8a064a4-fd32-11f0-9fbf-467786e86c71/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
+ "/AppleInternal/Library/BuildRoots/f8a064a4-fd32-11f0-9fbf-467786e86c71/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/RedBlackTree.h"
+ "/AppleInternal/Library/BuildRoots/f8a064a4-fd32-11f0-9fbf-467786e86c71/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/SinglyLinkedListWithTail.h"
+ "/AppleInternal/Library/BuildRoots/f8a064a4-fd32-11f0-9fbf-467786e86c71/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "/AppleInternal/Library/BuildRoots/f8a064a4-fd32-11f0-9fbf-467786e86c71/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakPtr.h"
+ "/AppleInternal/Library/BuildRoots/f8a064a4-fd32-11f0-9fbf-467786e86c71/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
+ "/AppleInternal/Library/BuildRoots/f8a064a4-fd32-11f0-9fbf-467786e86c71/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
+ "/AppleInternal/Library/BuildRoots/f8a064a4-fd32-11f0-9fbf-467786e86c71/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
+ "JSC::Wasm::Parser<void>::PartialResult JSC::Wasm::SectionParser::parseData()"
+ "JSC::Wasm::Parser<void>::PartialResult JSC::Wasm::SectionParser::parseElement()"
+ "JSC::Wasm::Parser<void>::PartialResult JSC::Wasm::SectionParser::parseException()"
+ "JSC::Wasm::Parser<void>::PartialResult JSC::Wasm::SectionParser::parseExport()"
+ "JSC::Wasm::Parser<void>::PartialResult JSC::Wasm::SectionParser::parseFunction()"
+ "JSC::Wasm::Parser<void>::PartialResult JSC::Wasm::SectionParser::parseImport()"
+ "JSC::Wasm::Parser<void>::PartialResult JSC::Wasm::SectionParser::parseType()"
- " type indices"
- "/AppleInternal/Library/BuildRoots/7281795f-03fd-11f0-b8c4-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/Assertions.h"
- "/AppleInternal/Library/BuildRoots/7281795f-03fd-11f0-b8c4-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
- "/AppleInternal/Library/BuildRoots/7281795f-03fd-11f0-b8c4-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/Deque.h"
- "/AppleInternal/Library/BuildRoots/7281795f-03fd-11f0-b8c4-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/IndexMap.h"
- "/AppleInternal/Library/BuildRoots/7281795f-03fd-11f0-b8c4-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/Liveness.h"
- "/AppleInternal/Library/BuildRoots/7281795f-03fd-11f0-b8c4-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/LockAlgorithmInlines.h"
- "/AppleInternal/Library/BuildRoots/7281795f-03fd-11f0-b8c4-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/NaturalLoops.h"
- "/AppleInternal/Library/BuildRoots/7281795f-03fd-11f0-b8c4-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
- "/AppleInternal/Library/BuildRoots/7281795f-03fd-11f0-b8c4-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/RedBlackTree.h"
- "/AppleInternal/Library/BuildRoots/7281795f-03fd-11f0-b8c4-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/SinglyLinkedListWithTail.h"
- "/AppleInternal/Library/BuildRoots/7281795f-03fd-11f0-b8c4-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "/AppleInternal/Library/BuildRoots/7281795f-03fd-11f0-b8c4-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakPtr.h"
- "/AppleInternal/Library/BuildRoots/7281795f-03fd-11f0-b8c4-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
- "/AppleInternal/Library/BuildRoots/7281795f-03fd-11f0-b8c4-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
- "/AppleInternal/Library/BuildRoots/7281795f-03fd-11f0-b8c4-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS16.7.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"

```


</details>

## EOF
