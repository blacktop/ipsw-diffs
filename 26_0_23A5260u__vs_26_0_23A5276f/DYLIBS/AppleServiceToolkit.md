## AppleServiceToolkit

> `/System/Library/PrivateFrameworks/AppleServiceToolkit.framework/AppleServiceToolkit`

```diff

-203.0.0.0.0
-  __TEXT.__text: 0x2d1f8
-  __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_methlist: 0x37a4
+211.0.0.0.0
+  __TEXT.__text: 0x2d5c4
+  __TEXT.__auth_stubs: 0x740
+  __TEXT.__objc_methlist: 0x3804
   __TEXT.__const: 0x164
-  __TEXT.__cstring: 0x2a6d
+  __TEXT.__cstring: 0x2a91
   __TEXT.__oslogstring: 0x215e
-  __TEXT.__gcc_except_tab: 0x13e0
-  __TEXT.__unwind_info: 0xc60
-  __TEXT.__objc_classname: 0x748
-  __TEXT.__objc_methname: 0x75ca
-  __TEXT.__objc_methtype: 0x1ab6
-  __TEXT.__objc_stubs: 0x5a80
+  __TEXT.__gcc_except_tab: 0x13f4
+  __TEXT.__unwind_info: 0xc70
+  __TEXT.__objc_classname: 0x74a
+  __TEXT.__objc_methname: 0x76bb
+  __TEXT.__objc_methtype: 0x1ac4
+  __TEXT.__objc_stubs: 0x5ae0
   __DATA_CONST.__got: 0x358
-  __DATA_CONST.__const: 0xb70
+  __DATA_CONST.__const: 0xb90
   __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c20
+  __DATA_CONST.__objc_selrefs: 0x1c48
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_arraydata: 0x110
-  __AUTH_CONST.__auth_got: 0x3a8
-  __AUTH_CONST.__const: 0x2c0
-  __AUTH_CONST.__cfstring: 0x2b80
-  __AUTH_CONST.__objc_const: 0x61f0
+  __AUTH_CONST.__auth_got: 0x3b0
+  __AUTH_CONST.__const: 0x2e0
+  __AUTH_CONST.__cfstring: 0x2b40
+  __AUTH_CONST.__objc_const: 0x6250
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x11f8
-  __DATA.__objc_ivar: 0x394
+  __DATA.__objc_ivar: 0x39c
   __DATA.__data: 0x800
   __DATA.__bss: 0x148
   __DATA_DIRTY.__objc_data: 0x1b8

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
-  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CheckerBoardServices.framework/CheckerBoardServices
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 35D63EBC-FF2F-3797-B277-F67DB3F05C51
-  Functions: 1223
-  Symbols:   4488
-  CStrings:  2615
+  UUID: 72BD8D43-AFA6-3D0B-9EC8-96F662400991
+  Functions: 1232
+  Symbols:   4500
+  CStrings:  2623
 
Symbols:
+ +[ASTTestAutomation conditionallyPostAccessibilityNotification:argument:]
+ -[ASTIdentity serialNumber]
+ -[ASTIdentity setSerialNumber:]
+ -[ASTRemoteServerSession clientAbortCompletion]
+ -[ASTRemoteServerSession idleWithCompletion:]
+ -[ASTRemoteServerSession setClientAbortCompletion:]
+ -[ASTSession idleWithCompletion:]
+ -[ASTSessionInfo .cxx_destruct]
+ -[ASTSessionInfo deviceSerialNumber]
+ -[ASTSessionInfo initWithQueuedSuiteType:isGuided:deviceSerialNumber:sessionType:]
+ GCC_except_table101
+ GCC_except_table25
+ GCC_except_table28
+ GCC_except_table31
+ GCC_except_table33
+ GCC_except_table37
+ GCC_except_table40
+ GCC_except_table44
+ GCC_except_table47
+ GCC_except_table49
+ GCC_except_table51
+ GCC_except_table56
+ GCC_except_table59
+ GCC_except_table61
+ GCC_except_table67
+ GCC_except_table70
+ GCC_except_table72
+ GCC_except_table75
+ GCC_except_table77
+ GCC_except_table81
+ GCC_except_table88
+ GCC_except_table91
+ GCC_except_table93
+ GCC_except_table95
+ GCC_except_table97
+ GCC_except_table99
+ _OBJC_IVAR_$_ASTIdentity._serialNumber
+ _OBJC_IVAR_$_ASTRemoteServerSession._clientAbortCompletion
+ _OBJC_IVAR_$_ASTSessionInfo._deviceSerialNumber
+ ___28-[ASTSession startWithMode:]_block_invoke.23
+ ___28-[ASTSession startWithMode:]_block_invoke.25
+ ___28-[ASTSession startWithMode:]_block_invoke.26
+ ___28-[ASTSession startWithMode:]_block_invoke.26.cold.1
+ ___28-[ASTSession startWithMode:]_block_invoke.26.cold.2
+ ___28-[ASTSession startWithMode:]_block_invoke.28
+ ___28-[ASTSession startWithMode:]_block_invoke.28.cold.1
+ ___28-[ASTSession startWithMode:]_block_invoke.28.cold.2
+ ___28-[ASTSession startWithMode:]_block_invoke.29
+ ___block_descriptor_32_e8_v16?0q8l
+ ___block_descriptor_48_e8_32s40bs_e68_v68?0B8B12i16q20"NSString"28"NSString"36q44"NSURL"52"NSError"60ls32l8s40l8
+ _dlclose
+ _dlsym
+ _objc_msgSend$conditionallyPostAccessibilityNotification:argument:
+ _objc_msgSend$deviceSerialNumber
+ _objc_msgSend$idleWithCompletion:
+ _objc_msgSend$initWithQueuedSuiteType:isGuided:deviceSerialNumber:sessionType:
+ _objc_msgSend$serialNumber
+ _objc_msgSend$setSerialNumber:
- -[ASTSessionInfo deviceIndex]
- -[ASTSessionInfo initWithQueuedSuiteType:isGuided:deviceIndex:sessionType:]
- GCC_except_table100
- GCC_except_table18
- GCC_except_table29
- GCC_except_table36
- GCC_except_table39
- GCC_except_table43
- GCC_except_table45
- GCC_except_table46
- GCC_except_table50
- GCC_except_table53
- GCC_except_table58
- GCC_except_table66
- GCC_except_table69
- GCC_except_table71
- GCC_except_table74
- GCC_except_table76
- GCC_except_table78
- GCC_except_table87
- GCC_except_table90
- GCC_except_table92
- GCC_except_table94
- GCC_except_table96
- GCC_except_table98
- _OBJC_IVAR_$_ASTSessionInfo._deviceIndex
- _UIAccessibilityPostNotification
- ___28-[ASTSession startWithMode:]_block_invoke.21
- ___28-[ASTSession startWithMode:]_block_invoke.22
- ___28-[ASTSession startWithMode:]_block_invoke.22.cold.1
- ___28-[ASTSession startWithMode:]_block_invoke.22.cold.2
- ___28-[ASTSession startWithMode:]_block_invoke.24
- ___28-[ASTSession startWithMode:]_block_invoke.24.cold.1
- ___28-[ASTSession startWithMode:]_block_invoke.24.cold.2
- ___28-[ASTSession startWithMode:]_block_invoke.27
- ___block_descriptor_40_e8_32bs_e68_v68?0B8B12i16q20"NSString"28"NSString"36q44"NSURL"52"NSError"60ls32l8
- _objc_msgSend$deviceIndex
- _objc_msgSend$initWithQueuedSuiteType:isGuided:deviceIndex:sessionType:
- _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
CStrings:
+ "!"
+ "@44@0:8q16B24@28q36"
+ "T@\"NSString\",&,N,V_serialNumber"
+ "T@\"NSString\",R,N,V_deviceSerialNumber"
+ "T@?,C,N,V_clientAbortCompletion"
+ "UIAccessibilityPostNotification"
+ "[ASTSessionInfo queuedSuiteType: %@, isGuided: %d, deviceSerialNumber: %@, sessionType: %@]"
+ "_clientAbortCompletion"
+ "_deviceSerialNumber"
+ "_serialNumber"
+ "clientAbortCompletion"
+ "conditionallyPostAccessibilityNotification:argument:"
+ "deviceSerialNumber"
+ "idleWithCompletion:"
+ "initWithQueuedSuiteType:isGuided:deviceSerialNumber:sessionType:"
+ "setClientAbortCompletion:"
+ "setSerialNumber:"
+ "v28@0:8I16@20"
- "."
- "@40@0:8q16B24i28q32"
- "Ti,R,N,V_deviceIndex"
- "[ASTSessionInfo queuedSuiteType: %@, isGuided: %d, deviceIndex: %d sessionType: %@]"
- "_"
- "_deviceIndex"
- "initWithQueuedSuiteType:isGuided:deviceIndex:sessionType:"
- "stringByReplacingOccurrencesOfString:withString:"

```
