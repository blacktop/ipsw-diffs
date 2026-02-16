## IOHIDLib

> `/System/Library/Extensions/IOHIDFamily.kext/PlugIns/IOHIDLib.plugin/IOHIDLib`

```diff

-2222.80.22.0.0
-  __TEXT.__text: 0xde68
-  __TEXT.__auth_stubs: 0x980
+2238.100.58.0.0
+  __TEXT.__text: 0xe438
+  __TEXT.__auth_stubs: 0x950
   __TEXT.__objc_methlist: 0x7d8
-  __TEXT.__const: 0xa0
-  __TEXT.__oslogstring: 0x9ca
-  __TEXT.__cstring: 0xb0d
-  __TEXT.__gcc_except_tab: 0x318
+  __TEXT.__const: 0xa8
+  __TEXT.__oslogstring: 0xa0f
+  __TEXT.__cstring: 0xb25
+  __TEXT.__gcc_except_tab: 0x314
   __TEXT.__dof_iohidfami: 0x28d
-  __TEXT.__unwind_info: 0x448
-  __TEXT.__objc_classname: 0xc7
-  __TEXT.__objc_methname: 0x11a8
-  __TEXT.__objc_methtype: 0xbdb
-  __TEXT.__objc_stubs: 0x1340
-  __DATA_CONST.__got: 0x100
+  __TEXT.__unwind_info: 0x450
+  __TEXT.__objc_classname: 0xca
+  __TEXT.__objc_methname: 0x1204
+  __TEXT.__objc_methtype: 0xbdd
+  __TEXT.__objc_stubs: 0x13c0
+  __DATA_CONST.__got: 0x108
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x528
+  __DATA_CONST.__objc_selrefs: 0x548
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x4d8
+  __AUTH_CONST.__auth_got: 0x4c0
   __AUTH_CONST.__const: 0xb8
-  __AUTH_CONST.__cfstring: 0x1140
-  __AUTH_CONST.__objc_const: 0x11c0
+  __AUTH_CONST.__cfstring: 0x1160
+  __AUTH_CONST.__objc_const: 0x1240
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x190
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x144
+  __DATA.__objc_ivar: 0x154
   __DATA.__common: 0x4
   __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0x190

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DA34D4A6-9BC1-3CD1-B984-6D7807173D50
-  Functions: 350
-  Symbols:   335
-  CStrings:  712
+  UUID: F5AEC395-505A-3151-B5D8-2D8AF808C4A3
+  Functions: 370
+  Symbols:   337
+  CStrings:  722
 
Symbols:
+ OBJC_IVAR_$_IOHIDDeviceClass._pendingCallbacks
+ OBJC_IVAR_$_IOHIDTransactionClass._callbackLock
+ OBJC_IVAR_$_IOHIDTransactionClass._pendingCallbacks
+ OBJC_IVAR_$_IOHIDUPSClass._powerFeaturePollInterval
+ _OBJC_CLASS_$_NSValue
+ _objc_retain_x22
+ _objc_retain_x26
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x23
- _objc_retain_x8
- _objc_retain_x9
CStrings:
+ "Create timer for polling feature reports (interval: %.2f sec)"
+ "PowerFeaturePollRateSec"
+ "Using custom power feature poll rate: %.2f sec"
+ "_pendingCallbacks"
+ "_powerFeaturePollInterval"
+ "copy"
+ "d"
+ "doubleValue"
+ "pointerValue"
+ "ub"
+ "valueWithPointer:"
- "1"
- "Create time for polling feature reports"
- "ua"

```
