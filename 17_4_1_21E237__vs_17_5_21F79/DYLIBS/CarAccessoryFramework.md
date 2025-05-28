## CarAccessoryFramework

> `/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`

```diff

-294.16.1.0.0
-  __TEXT.__text: 0x7bd04
+294.19.2.0.0
+  __TEXT.__text: 0x7be08
   __TEXT.__auth_stubs: 0x560
-  __TEXT.__objc_methlist: 0xc9b0
+  __TEXT.__objc_methlist: 0xc9e8
   __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x4a50
+  __TEXT.__cstring: 0x4a72
   __TEXT.__gcc_except_tab: 0x540
-  __TEXT.__oslogstring: 0x2161
+  __TEXT.__oslogstring: 0x2183
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x1cdc
-  __TEXT.__objc_classname: 0x2472
-  __TEXT.__objc_methname: 0x11798
+  __TEXT.__unwind_info: 0x1ce8
+  __TEXT.__objc_classname: 0x2475
+  __TEXT.__objc_methname: 0x11834
   __TEXT.__objc_methtype: 0x2d00
-  __TEXT.__objc_stubs: 0xcf20
+  __TEXT.__objc_stubs: 0xcf60
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x1860
   __DATA_CONST.__objc_classlist: 0x838

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x418
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x29f68
-  __DATA_CONST.__objc_selrefs: 0x4850
+  __DATA_CONST.__objc_const: 0x29fd0
+  __DATA_CONST.__objc_selrefs: 0x4870
   __DATA_CONST.__objc_protorefs: 0x3b0
   __DATA_CONST.__objc_classrefs: 0x7c0
   __DATA_CONST.__objc_superrefs: 0xaa0

   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__auth_got: 0x2c0
-  __AUTH.__objc_data: 0x2080
-  __DATA.__objc_ivar: 0x39c
+  __AUTH.__objc_data: 0x1a90
+  __DATA.__objc_ivar: 0x3a4
   __DATA.__data: 0x3140
-  __DATA.__bss: 0x328
-  __DATA_DIRTY.__objc_data: 0x31b0
-  __DATA_DIRTY.__bss: 0x40
+  __DATA.__bss: 0x2d8
+  __DATA_DIRTY.__objc_data: 0x37a0
+  __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4313
-  Symbols:   14899
-  CStrings:  5096
+  Functions: 4319
+  Symbols:   14915
+  CStrings:  5107
 
Symbols:
+ -[CAFCarManager _closeConnection]
+ -[CAFCarManager _closeConnection].cold.1
+ -[_CAFCarDataClientProxy invalidate]
+ -[_CAFCarDataClientProxy invalidatedLock]
+ -[_CAFCarDataClientProxy invalidated]
+ -[_CAFCarDataClientProxy setInvalidatedLock:]
+ GCC_except_table13
+ GCC_except_table43
+ _OBJC_IVAR_$__CAFCarDataClientProxy._invalidated
+ _OBJC_IVAR_$__CAFCarDataClientProxy._invalidatedLock
+ ___45-[_CAFCarDataClientProxy initWithCarManager:]_block_invoke.183.cold.1
+ ___45-[_CAFCarDataClientProxy initWithCarManager:]_block_invoke.183.cold.2
+ ___45-[_CAFCarDataClientProxy initWithCarManager:]_block_invoke.184
+ _objc_msgSend$_closeConnection
+ _objc_msgSend$invalidated
- GCC_except_table42
- ___45-[_CAFCarDataClientProxy initWithCarManager:]_block_invoke.181
- ___45-[_CAFCarDataClientProxy initWithCarManager:]_block_invoke.181.cold.1
- ___45-[_CAFCarDataClientProxy initWithCarManager:]_block_invoke.182.cold.2
CStrings:
+ "\x11\x12"
+ "%s %{public}@: connection cleared"
+ "-[CAFCarManager _closeConnection]"
+ "TB,R,N,V_invalidated"
+ "T{os_unfair_lock_s=I},N,V_invalidatedLock"
+ "_closeConnection"
+ "_invalidated"
+ "_invalidatedLock"
+ "invalidated"
+ "invalidatedLock"
+ "setInvalidatedLock:"

```
