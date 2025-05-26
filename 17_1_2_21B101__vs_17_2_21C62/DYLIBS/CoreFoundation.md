## CoreFoundation

> `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

```diff

-2106.0.0.0.0
-  __TEXT.__text: 0x1bbb58
+2202.0.0.0.0
+  __TEXT.__text: 0x1bbcf8
   __TEXT.__auth_stubs: 0x31a0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x769c
   __TEXT.__const: 0x185a38
   __TEXT.__oslogstring: 0x5882
   __TEXT.__cstring: 0x14aed8
-  __TEXT.__gcc_except_tab: 0x347c
+  __TEXT.__gcc_except_tab: 0x34a4
   __TEXT.__ustring: 0x480
   __TEXT.__dof_CFRunLoop: 0x964
   __TEXT.__dof_Cocoa_Aut: 0x486
-  __TEXT.__unwind_info: 0x550c
+  __TEXT.__unwind_info: 0x5518
   __TEXT.__objc_classname: 0xa76
-  __TEXT.__objc_methname: 0x7b30
+  __TEXT.__objc_methname: 0x7b56
   __TEXT.__objc_methtype: 0x779b8
   __TEXT.__objc_stubs: 0x5620
-  __DATA_CONST.__const: 0x279fe0
+  __DATA_CONST.__const: 0x27a008
   __DATA_CONST.__objc_classlist: 0x460
   __DATA_CONST.__objc_nlclslist: 0x58
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6128
+  __DATA_CONST.__objc_const: 0x6168
   __DATA_CONST.__objc_selrefs: 0x2438
   __DATA_CONST.__got: 0x390
   __DATA_CONST.__objc_arraydata: 0x1520
   __AUTH_CONST.__const_cfobj2: 0x40
-  __AUTH_CONST.__const: 0x4898
+  __AUTH_CONST.__const: 0x4878
   __AUTH_CONST.__cfstring: 0x140d60
   __AUTH_CONST.__objc_const: 0x3a88
   __AUTH_CONST.__auth_ptr: 0x1f0

   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x258
   __DATA.__objc_superrefs: 0x2c0
-  __DATA.__objc_ivar: 0x4f4
+  __DATA.__objc_ivar: 0x4fc
   __DATA.__data: 0xaa0
   __DATA.__thread_vars: 0x18
   __DATA.__cf_except_bt: 0x2000

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7593
-  Symbols:   19124
-  CStrings:  55626
+  Functions: 7594
+  Symbols:   19129
+  CStrings:  55628
 
Symbols:
+ -[CFPDObserverOnlyTombstone _sendNotificationToConnection:]
+ GCC_except_table170
+ GCC_except_table199
+ GCC_except_table206
+ _OBJC_IVAR_$_CFPDObserverOnlyTombstone._lock
+ _OBJC_IVAR_$_CFPDObserverOnlyTombstone._needToNotify
+ _OBJC_IVAR_$_CFPDObserverOnlyTombstone._notificationInProgress
+ ___59-[CFPDObserverOnlyTombstone _sendNotificationToConnection:]_block_invoke
+ ___block_descriptor_56_e8_32o40o48w_e33_v16?0"NSObject<OS_xpc_object>"8lw48l8s32l8s40l8
- GCC_except_table198
- GCC_except_table205
- _OBJC_IVAR_$_CFPDObserverOnlyTombstone._observingConnectionsLock
- ___44-[CFPDObserverOnlyTombstone notifyObservers]_block_invoke_5
- ___block_literal_global.305
CStrings:
+ "_needToNotify"
+ "_notificationInProgress"

```
