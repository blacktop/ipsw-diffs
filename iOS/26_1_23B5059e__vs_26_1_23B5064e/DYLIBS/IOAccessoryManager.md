## IOAccessoryManager

> `/System/Library/PrivateFrameworks/IOAccessoryManager.framework/IOAccessoryManager`

```diff

-1044.40.1.0.0
-  __TEXT.__text: 0x25c68
+1044.40.2.0.0
+  __TEXT.__text: 0x25d74
   __TEXT.__auth_stubs: 0xbe0
-  __TEXT.__objc_methlist: 0x3234
+  __TEXT.__objc_methlist: 0x326c
   __TEXT.__const: 0x8b8
-  __TEXT.__oslogstring: 0x540c
+  __TEXT.__oslogstring: 0x5435
   __TEXT.__cstring: 0x4a3d
   __TEXT.__ustring: 0x154
   __TEXT.__gcc_except_tab: 0x44
   __TEXT.__unwind_info: 0x578
   __TEXT.__objc_classname: 0x1d4
-  __TEXT.__objc_methname: 0x8d36
+  __TEXT.__objc_methname: 0x8df3
   __TEXT.__objc_methtype: 0xe7b
-  __TEXT.__objc_stubs: 0x48c0
+  __TEXT.__objc_stubs: 0x4960
   __DATA_CONST.__got: 0x2f8
   __DATA_CONST.__const: 0x420
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c90
+  __DATA_CONST.__objc_selrefs: 0x1cb8
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x600
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x31a0
-  __AUTH_CONST.__objc_const: 0x6ab8
+  __AUTH_CONST.__objc_const: 0x6b18
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x79c
+  __DATA.__objc_ivar: 0x7a4
   __DATA.__data: 0x248
   __DATA.__common: 0x58
   __DATA.__bss: 0x28

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B42A2694-AB5E-351D-A46A-E56E7B56F8DD
-  Functions: 1368
-  Symbols:   4329
-  CStrings:  3030
+  UUID: 247972AA-D52A-3EDA-A585-EDE082B4D9B3
+  Functions: 1373
+  Symbols:   4346
+  CStrings:  3040
 
Symbols:
+ -[IOPortLDCMManagerV4 disableOVPInterrupts]
+ -[IOPortLDCMManagerV4 ovpErrorCount]
+ -[IOPortLDCMManagerV4 ovpInterruptsDisabled]
+ -[IOPortLDCMManagerV4 setOvpErrorCount:]
+ -[IOPortLDCMManagerV4 setOvpInterruptsDisabled:]
+ _OBJC_IVAR_$_IOPortLDCMManagerV4._ovpErrorCount
+ _OBJC_IVAR_$_IOPortLDCMManagerV4._ovpInterruptsDisabled
+ _objc_msgSend$disableOVPInterrupts
+ _objc_msgSend$ovpErrorCount
+ _objc_msgSend$ovpInterruptsDisabled
+ _objc_msgSend$setOvpErrorCount:
+ _objc_msgSend$setOvpInterruptsDisabled:
CStrings:
+ "LDCM - Request to disable OVP interrupts"
+ "TB,N,V_ovpInterruptsDisabled"
+ "TC,N,V_ovpErrorCount"
+ "_ovpErrorCount"
+ "_ovpInterruptsDisabled"
+ "disableOVPInterrupts"
+ "ovpErrorCount"
+ "ovpInterruptsDisabled"
+ "setOvpErrorCount:"
+ "setOvpInterruptsDisabled:"

```
