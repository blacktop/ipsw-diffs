## DesktopServicesPriv

> `/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesPriv`

```diff

-1631.1.3.0.0
-  __TEXT.__text: 0xf8e00
+1631.2.2.0.0
+  __TEXT.__text: 0xf8f34
   __TEXT.__auth_stubs: 0x2150
-  __TEXT.__objc_methlist: 0x1388
-  __TEXT.__const: 0x1fd8
-  __TEXT.__gcc_except_tab: 0x132ac
+  __TEXT.__objc_methlist: 0x13d0
+  __TEXT.__const: 0x1fe8
+  __TEXT.__gcc_except_tab: 0x132dc
   __TEXT.__cstring: 0x3888
-  __TEXT.__oslogstring: 0x1acd
+  __TEXT.__oslogstring: 0x1ad7
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x8068
+  __TEXT.__unwind_info: 0x806c
   __TEXT.__eh_frame: 0x36c
-  __TEXT.__objc_classname: 0x35d
-  __TEXT.__objc_methname: 0x43b8
-  __TEXT.__objc_methtype: 0x4c74
-  __TEXT.__objc_stubs: 0x3560
+  __TEXT.__objc_classname: 0x387
+  __TEXT.__objc_methname: 0x43d2
+  __TEXT.__objc_methtype: 0x4cbf
+  __TEXT.__objc_stubs: 0x35a0
   __DATA_CONST.__got: 0x640
   __DATA_CONST.__const: 0x6c0
-  __DATA_CONST.__objc_classlist: 0xf0
+  __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x60
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2228
+  __DATA_CONST.__objc_const: 0x23b8
   __DATA_CONST.__objc_selrefs: 0x1170
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__cfstring: 0x1460
-  __AUTH_CONST.__objc_const: 0xa18
+  __AUTH_CONST.__objc_const: 0xa60
   __AUTH_CONST.__const: 0x37a0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x10c0
-  __AUTH.__objc_data: 0x5a0
+  __AUTH.__objc_data: 0x5f0
   __AUTH.__const_weak: 0x4e8
   __AUTH.__data: 0x30
   __DATA.__got_weak: 0x1b0
   __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x1d0
+  __DATA.__objc_classrefs: 0x1d8
   __DATA.__objc_superrefs: 0xa8
-  __DATA.__objc_ivar: 0x168
-  __DATA.__data: 0x5ac
+  __DATA.__objc_ivar: 0x170
+  __DATA.__data: 0x60c
   __DATA.__bss: 0x13f8
   __DATA.__common: 0xc0
   __DATA_DIRTY.__const: 0x8

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AE03C0D0-49EB-336B-B2C7-8CD7EF26F9A5
-  Functions: 5323
-  Symbols:   13210
-  CStrings:  1967
+  UUID: 74257A84-A068-3A34-AAC4-6F71853BA7B3
+  Functions: 5328
+  Symbols:   13235
+  CStrings:  1977
 
Symbols:
+ -[_FINullObserver childNodePropertyChanged:forProperty:]
+ -[_FINullObserver childNodesAdded:]
+ -[_FINullObserver childNodesDeleted:]
+ -[_FINullObserver nodeDeleted:]
+ -[_FINullObserver nodePropertyChanged:forProperty:]
+ _OBJC_CLASS_$__FINullObserver
+ _OBJC_IVAR_$_FINodeObserver._parentObserver
+ _OBJC_IVAR_$_FINodeObserver._parentUbiquityCount
+ _OBJC_METACLASS_$__FINullObserver
+ __OBJC_$_INSTANCE_METHODS__FINullObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FINodeObserverProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FINodeObserverProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FINodeObserverProtocol
+ __OBJC_CLASS_PROTOCOLS_$__FINullObserver
+ __OBJC_CLASS_RO_$__FINullObserver
+ __OBJC_LABEL_PROTOCOL_$_FINodeObserverProtocol
+ __OBJC_METACLASS_RO_$__FINullObserver
+ __OBJC_PROTOCOL_$_FINodeObserverProtocol
+ ___49+[FINodeObserver observerForFINode:withObserver:]_block_invoke.332
+ _objc_msgSend$observerForFINode:withObserver:
+ _objc_msgSend$stopObserving:
- ___49+[FINodeObserver observerForFINode:withObserver:]_block_invoke.316
CStrings:
+ "\x01!"
+ "@\"FINodeObserver\""
+ "FINodeObserverProtocol"
+ "[%@] startObserving %@ (0x%x)"
+ "[%@] stopObserving %@ (0x%x)"
+ "_FINullObserver"
+ "_parentObserver"
+ "_parentUbiquityCount"
+ "v24@0:8@\"FINode\"16"
+ "v28@0:8@\"FINode\"16I24"
+ "v28@0:8@16I24"
- "startObserving %@ (0x%x)"
- "stopObserving %@ (0x%x)"

```
