## AppleLatticeSupport

> `/System/Library/PrivateFrameworks/AppleLatticeSupport.framework/AppleLatticeSupport`

```diff

-156.0.0.0.0
-  __TEXT.__text: 0xf88
+156.80.2.0.0
+  __TEXT.__text: 0x10ec
   __TEXT.__auth_stubs: 0x300
-  __TEXT.__objc_methlist: 0x68
+  __TEXT.__objc_methlist: 0x80
   __TEXT.__const: 0x58
-  __TEXT.__gcc_except_tab: 0x174
-  __TEXT.__cstring: 0x20c
+  __TEXT.__gcc_except_tab: 0x170
+  __TEXT.__cstring: 0x245
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0xf8
+  __TEXT.__unwind_info: 0x100
   __TEXT.__objc_classname: 0x19
-  __TEXT.__objc_methname: 0x162
-  __TEXT.__objc_methtype: 0xeb
+  __TEXT.__objc_methname: 0x194
+  __TEXT.__objc_methtype: 0x102
   __TEXT.__objc_stubs: 0x100
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x70
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x80
+  __DATA_CONST.__objc_selrefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x190

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 71FD5E91-E5A1-35BE-AFCD-D3CBEBDBC60B
-  Functions: 22
-  Symbols:   142
-  CStrings:  75
+  UUID: 532946FF-EFD7-3F58-8AF5-9F0D545603E0
+  Functions: 25
+  Symbols:   148
+  CStrings:  81
 
Symbols:
+ -[AppleLatticeServiceRef getLatticeHealthStatus]
+ -[AppleLatticeServiceRef startGetInterfaceUpdateEvents:]
+ -[AppleLatticeServiceRef startWithoutCallbacks]
+ GCC_except_table21
+ GCC_except_table9
+ __ZN12_GLOBAL__N_113LatticeClient11openServiceEv
+ ___56-[AppleLatticeServiceRef startGetInterfaceUpdateEvents:]_block_invoke
+ ___56-[AppleLatticeServiceRef startGetInterfaceUpdateEvents:]_block_invoke_2
+ ___56-[AppleLatticeServiceRef startGetInterfaceUpdateEvents:]_block_invoke_3
- -[AppleLatticeServiceRef getInterfaceUpdateEvents:]
- GCC_except_table15
- GCC_except_table7
- ___51-[AppleLatticeServiceRef getInterfaceUpdateEvents:]_block_invoke
- ___51-[AppleLatticeServiceRef getInterfaceUpdateEvents:]_block_invoke_2
- ___51-[AppleLatticeServiceRef getInterfaceUpdateEvents:]_block_invoke_3
Functions:
+ -[AppleLatticeServiceRef startGetInterfaceUpdateEvents:]
- ___51-[AppleLatticeServiceRef getInterfaceUpdateEvents:]_block_invoke
+ -[AppleLatticeServiceRef startWithoutCallbacks]
+ -[AppleLatticeServiceRef getLatticeHealthStatus]
+ __ZN12_GLOBAL__N_113LatticeClient11openServiceEv
~ __ZN12_GLOBAL__N_113LatticeClient14onNotificationEy : 504 -> 524
CStrings:
+ "B16@0:8"
+ "Unable to fetch health status: %x"
+ "Unable to open service"
+ "getLatticeHealthStatus"
+ "startGetInterfaceUpdateEvents:"
+ "startWithoutCallbacks"
+ "{?=BBQQ}16@0:8"
- "getInterfaceUpdateEvents:"

```
