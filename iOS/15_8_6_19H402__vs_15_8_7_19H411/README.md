# 15.8.6 (19H402) .vs 15.8.7 (19H411)

## IPSWs

- `iPodtouch_7_15.8.6_19H402_Restore.ipsw`
- `iPodtouch_7_15.8.7_19H411_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 15.8.6 *(19H402)* | 21.6.0 | 8020.241.42~8 | Sun, 15Oct2023 00:18:06 PDT |
| 15.8.7 *(19H411)* | 21.6.0 | 8020.241.44~1 | Fri, 06Mar2026 20:59:07 PST |

## MachO

### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### MobileMail

>  `/private/var/staged_system_apps/MobileMail.app/MobileMail`

```diff

 3696.120.41.2.6
-  __TEXT.__text: 0x26d248
+  __TEXT.__text: 0x26d244
   __TEXT.__stubs: 0xf3c
   __TEXT.__objc_methlist: 0x1d518
   __TEXT.__gcc_except_tab: 0x55d24

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: A77691A4-193E-3B3C-9F75-655B9464540C
+  UUID: E5722076-BBDC-30DF-9E4C-465B1B34230C
   Functions: 12009
   Symbols:   1451
   CStrings:  19688
Functions:
~ sub_10020ab6c -> sub_10020ab70 : 1820 -> 1816

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 15.8.6 *(19H402)* | 7613.7.1.0.16 |
| 15.8.7 *(19H411)* | 7613.7.1.0.17 |

### Dylibs

#### ⬆️ Updated (4)

<details>
  <summary><i>View Updated</i></summary>

#### JavaScriptCore

>  `/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore`

```diff

-7613.7.1.0.16
-  __TEXT.__text: 0x1267a10
+7613.7.1.0.17
+  __TEXT.__text: 0x126781c
   __TEXT.__stubs: 0x1e6c
   __TEXT.__objc_methlist: 0x8f0
   __TEXT.__const: 0x6a3b8
-  __TEXT.__cstring: 0xa9c8b
+  __TEXT.__cstring: 0xa9eb6
   __TEXT.__oslogstring: 0x692
   __TEXT.__gcc_except_tab: 0x1970
   __TEXT.__unwind_info: 0x13a0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AEA65AD6-85DC-3026-B23B-2A6FCF9789B7
+  UUID: 2C7F4D31-EAA2-359C-B24B-A7911CFEF53C
   Functions: 25015
   Symbols:   51407
-  CStrings:  16033
+  CStrings:  16040
 
CStrings:
+ "/AppleInternal/Library/BuildRoots/20868aaf-f828-11f0-a0d4-b69ca7b7666f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS15.8.Internal.sdk/usr/local/include/wtf/Assertions.h"
+ "/AppleInternal/Library/BuildRoots/20868aaf-f828-11f0-a0d4-b69ca7b7666f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS15.8.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
+ "/AppleInternal/Library/BuildRoots/20868aaf-f828-11f0-a0d4-b69ca7b7666f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS15.8.Internal.sdk/usr/local/include/wtf/Deque.h"
+ "/AppleInternal/Library/BuildRoots/20868aaf-f828-11f0-a0d4-b69ca7b7666f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS15.8.Internal.sdk/usr/local/include/wtf/IndexMap.h"
+ "/AppleInternal/Library/BuildRoots/20868aaf-f828-11f0-a0d4-b69ca7b7666f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS15.8.Internal.sdk/usr/local/include/wtf/Liveness.h"
+ "/AppleInternal/Library/BuildRoots/20868aaf-f828-11f0-a0d4-b69ca7b7666f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS15.8.Internal.sdk/usr/local/include/wtf/LockAlgorithmInlines.h"
+ "/AppleInternal/Library/BuildRoots/20868aaf-f828-11f0-a0d4-b69ca7b7666f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS15.8.Internal.sdk/usr/local/include/wtf/NaturalLoops.h"
+ "/AppleInternal/Library/BuildRoots/20868aaf-f828-11f0-a0d4-b69ca7b7666f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS15.8.Internal.sdk/usr/local/include/wtf/RedBlackTree.h"
+ "/AppleInternal/Library/BuildRoots/20868aaf-f828-11f0-a0d4-b69ca7b7666f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS15.8.Internal.sdk/usr/local/include/wtf/SinglyLinkedListWithTail.h"
+ "/AppleInternal/Library/BuildRoots/20868aaf-f828-11f0-a0d4-b69ca7b7666f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS15.8.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "/AppleInternal/Library/BuildRoots/20868aaf-f828-11f0-a0d4-b69ca7b7666f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS15.8.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
+ "/AppleInternal/Library/BuildRoots/20868aaf-f828-11f0-a0d4-b69ca7b7666f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS15.8.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
+ "/AppleInternal/Library/BuildRoots/20868aaf-f828-11f0-a0d4-b69ca7b7666f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS15.8.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
+ "JSC::Wasm::Parser<void>::PartialResult JSC::Wasm::SectionParser::parseData()"
+ "JSC::Wasm::Parser<void>::PartialResult JSC::Wasm::SectionParser::parseElement()"
+ "JSC::Wasm::Parser<void>::PartialResult JSC::Wasm::SectionParser::parseException()"
+ "JSC::Wasm::Parser<void>::PartialResult JSC::Wasm::SectionParser::parseExport()"
+ "JSC::Wasm::Parser<void>::PartialResult JSC::Wasm::SectionParser::parseFunction()"
+ "JSC::Wasm::Parser<void>::PartialResult JSC::Wasm::SectionParser::parseImport()"
+ "JSC::Wasm::Parser<void>::PartialResult JSC::Wasm::SectionParser::parseType()"
- "/AppleInternal/Library/BuildRoots/b04af8ff-04b3-11f0-b0ac-fe9e33ca05fa/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS15.8.Internal.sdk/usr/local/include/wtf/Assertions.h"
- "/AppleInternal/Library/BuildRoots/b04af8ff-04b3-11f0-b0ac-fe9e33ca05fa/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS15.8.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
- "/AppleInternal/Library/BuildRoots/b04af8ff-04b3-11f0-b0ac-fe9e33ca05fa/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS15.8.Internal.sdk/usr/local/include/wtf/Deque.h"
- "/AppleInternal/Library/BuildRoots/b04af8ff-04b3-11f0-b0ac-fe9e33ca05fa/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS15.8.Internal.sdk/usr/local/include/wtf/IndexMap.h"
- "/AppleInternal/Library/BuildRoots/b04af8ff-04b3-11f0-b0ac-fe9e33ca05fa/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS15.8.Internal.sdk/usr/local/include/wtf/Liveness.h"
- "/AppleInternal/Library/BuildRoots/b04af8ff-04b3-11f0-b0ac-fe9e33ca05fa/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS15.8.Internal.sdk/usr/local/include/wtf/LockAlgorithmInlines.h"
- "/AppleInternal/Library/BuildRoots/b04af8ff-04b3-11f0-b0ac-fe9e33ca05fa/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS15.8.Internal.sdk/usr/local/include/wtf/NaturalLoops.h"
- "/AppleInternal/Library/BuildRoots/b04af8ff-04b3-11f0-b0ac-fe9e33ca05fa/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS15.8.Internal.sdk/usr/local/include/wtf/RedBlackTree.h"
- "/AppleInternal/Library/BuildRoots/b04af8ff-04b3-11f0-b0ac-fe9e33ca05fa/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS15.8.Internal.sdk/usr/local/include/wtf/SinglyLinkedListWithTail.h"
- "/AppleInternal/Library/BuildRoots/b04af8ff-04b3-11f0-b0ac-fe9e33ca05fa/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS15.8.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "/AppleInternal/Library/BuildRoots/b04af8ff-04b3-11f0-b0ac-fe9e33ca05fa/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS15.8.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
- "/AppleInternal/Library/BuildRoots/b04af8ff-04b3-11f0-b0ac-fe9e33ca05fa/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS15.8.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
- "/AppleInternal/Library/BuildRoots/b04af8ff-04b3-11f0-b0ac-fe9e33ca05fa/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS15.8.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"

```

#### AudioToolboxCore

>  `/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`

```diff

-1245.90.3.0.0
-  __TEXT.__text: 0x20d1e8
+1245.90.4.0.0
+  __TEXT.__text: 0x20d1fc
   __TEXT.__stubs: 0x2460
   __TEXT.__objc_methlist: 0x2830
   __TEXT.__const: 0x1cad0

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D64A1277-BD04-3C0C-B684-1DF59B20A781
+  UUID: 63282333-A176-370F-889A-76C015FC5A29
   Functions: 9051
   Symbols:   22203
   CStrings:  5850
Functions:
~ __ZN16AudibleAudioFile18OpenFromDataSourceEv : 5368 -> 5388

```

#### NotesShared

>  `/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared`

```diff

 2020.0.0.0.0
-  __TEXT.__text: 0x1e8f18
+  __TEXT.__text: 0x1e8ef8
   __TEXT.__stubs: 0x1b9c
   __TEXT.__objc_methlist: 0x10360
   __TEXT.__const: 0x3df0
   __TEXT.__cstring: 0xf296
   __TEXT.__oslogstring: 0x1014e
-  __TEXT.__gcc_except_tab: 0xe8d4
+  __TEXT.__gcc_except_tab: 0xe8d0
   __TEXT.__dlopen_cstrs: 0x2d0
   __TEXT.__ustring: 0x240
   __TEXT.__swift5_typeref: 0xc8a

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 93F69C1C-6111-3218-8FC7-5AE16F9937D7
+  UUID: 087F27B8-6FA2-387D-96A5-162EDC97903B
   Functions: 11011
   Symbols:   25383
   CStrings:  11692
Functions:
~ +[CRIndex indexForReplica:betweenIndex:andIndex:] : 1548 -> 1516

```

#### H264H8.videodecoder

>  `/System/Library/VideoDecoders/H264H8.videodecoder`

```diff

   __TEXT.__text: 0x19ae4
   __TEXT.__stubs: 0x834
   __TEXT.__const: 0x3d0
-  __TEXT.__cstring: 0x6c23
+  __TEXT.__cstring: 0x6c1a
   __TEXT.__gcc_except_tab: 0x94
   __TEXT.__unwind_info: 0x2ec
   __TEXT.__eh_frame: 0x80

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: D2F7EF6A-2F13-3674-A9E6-CC8A840226CA
+  UUID: 81FF1A56-2F61-32CA-B2C3-2705C52B92FD
   Functions: 181
   Symbols:   640
-  CStrings:  490
+  CStrings:  489
 
CStrings:
+ "21:21:51"
+ "Mar  6 2026"
- "21:38:28"
- "21:38:29"
- "Jun 25 2025"

```


</details>

## EOF
