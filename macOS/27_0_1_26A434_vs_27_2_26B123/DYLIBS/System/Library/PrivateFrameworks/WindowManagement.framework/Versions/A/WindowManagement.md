## WindowManagement

> `/System/Library/PrivateFrameworks/WindowManagement.framework/Versions/A/WindowManagement`

```diff

-462.0.8.402.0
-  __TEXT.__text: 0x13ce8
-  __TEXT.__objc_methlist: 0x2414
+462.1.41.404.0
+  __TEXT.__text: 0x14d98
+  __TEXT.__objc_methlist: 0x263c
   __TEXT.__const: 0x3ca
   __TEXT.__gcc_except_tab: 0x74
-  __TEXT.__cstring: 0x1226
+  __TEXT.__cstring: 0x124d
   __TEXT.__oslogstring: 0x1be
   __TEXT.__swift5_typeref: 0x169
   __TEXT.__swift5_reflstr: 0x2d

   __TEXT.__swift5_fieldmd: 0xb4
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x18
-  __TEXT.__unwind_info: 0x6a0
+  __TEXT.__unwind_info: 0x6f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x150
-  __DATA_CONST.__objc_classlist: 0x130
+  __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf70
+  __DATA_CONST.__objc_selrefs: 0x1048
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x100
-  __DATA_CONST.__objc_arraydata: 0x90
-  __DATA_CONST.__got: 0x290
+  __DATA_CONST.__objc_superrefs: 0x110
+  __DATA_CONST.__objc_arraydata: 0xc0
+  __DATA_CONST.__got: 0x2a0
   __AUTH_CONST.__const: 0x658
-  __AUTH_CONST.__cfstring: 0x1640
-  __AUTH_CONST.__objc_const: 0x4780
-  __AUTH_CONST.__objc_intobj: 0xd8
-  __AUTH_CONST.__objc_arrayobj: 0x1b0
+  __AUTH_CONST.__cfstring: 0x1760
+  __AUTH_CONST.__objc_const: 0x4b88
+  __AUTH_CONST.__objc_intobj: 0x120
+  __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__auth_got: 0x298
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_ivar: 0x31c
+  __AUTH.__objc_data: 0x640
+  __DATA.__objc_ivar: 0x348
   __DATA.__data: 0x300
   __DATA.__bss: 0x590
   __DATA_DIRTY.__objc_data: 0x640

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 845
-  Symbols:   1865
-  CStrings:  213
+  Functions: 889
+  Symbols:   1952
+  CStrings:  222
 
Symbols:
+ +[_WMCornerRadii supportsSecureCoding]
+ +[_WMWindowConstraints supportsSecureCoding]
+ -[WMClientWindowManager holdTearOffTabDragWithWindowIdentifier:]
+ -[WMClientWindowManager refreshTilingConstraintsWithWindowIdentifier:reply:]
+ -[WMClientWindowManager releaseTearOffTabDragWithWindowIdentifier:]
+ -[WMWindowPropertySnapshot cornerRadii]
+ -[WMWindowPropertySnapshot setCornerRadii:]
+ -[WMWindowPropertySnapshot setWindowConstraints:]
+ -[WMWindowPropertySnapshot windowConstraints]
+ -[_WMCornerRadii copyWithZone:]
+ -[_WMCornerRadii encodeWithCoder:]
+ -[_WMCornerRadii hash]
+ -[_WMCornerRadii initWithCoder:]
+ -[_WMCornerRadii initWithMinXMinY:maxXMinY:minXMaxY:maxXMaxY:]
+ -[_WMCornerRadii initWithUniformRadius:]
+ -[_WMCornerRadii isEqual:]
+ -[_WMCornerRadii maxXMaxY]
+ -[_WMCornerRadii maxXMinY]
+ -[_WMCornerRadii minXMaxY]
+ -[_WMCornerRadii minXMinY]
+ -[_WMWindow cornerRadii]
+ -[_WMWindow setCornerRadii:]
+ -[_WMWindow setWantsFourFingerGestures:]
+ -[_WMWindow setWantsMoreThanFourFingerGestures:]
+ -[_WMWindow setWantsThreeFingerGestures:]
+ -[_WMWindow setWindowConstraints:]
+ -[_WMWindow wantsFourFingerGestures]
+ -[_WMWindow wantsMoreThanFourFingerGestures]
+ -[_WMWindow wantsThreeFingerGestures]
+ -[_WMWindow windowConstraints]
+ -[_WMWindowConstraints copyWithZone:]
+ -[_WMWindowConstraints encodeWithCoder:]
+ -[_WMWindowConstraints hash]
+ -[_WMWindowConstraints initWithCoder:]
+ -[_WMWindowConstraints initWithMinSize:maxSize:preferredSize:]
+ -[_WMWindowConstraints isEqual:]
+ -[_WMWindowConstraints maxSize]
+ -[_WMWindowConstraints minSize]
+ -[_WMWindowConstraints preferredSize]
+ GCC_except_table67
+ GCC_except_table68
+ GCC_except_table85
+ OBJC_IVAR_$_WMWindowPropertySnapshot._cornerRadii
+ OBJC_IVAR_$_WMWindowPropertySnapshot._windowConstraints
+ OBJC_IVAR_$__WMCornerRadii._maxXMaxY
+ OBJC_IVAR_$__WMCornerRadii._maxXMinY
+ OBJC_IVAR_$__WMCornerRadii._minXMaxY
+ OBJC_IVAR_$__WMCornerRadii._minXMinY
+ OBJC_IVAR_$__WMWindow._cornerRadii
+ OBJC_IVAR_$__WMWindow._windowConstraints
+ OBJC_IVAR_$__WMWindowConstraints._maxSize
+ OBJC_IVAR_$__WMWindowConstraints._minSize
+ OBJC_IVAR_$__WMWindowConstraints._preferredSize
+ _OBJC_CLASS_$__WMCornerRadii
+ _OBJC_CLASS_$__WMWindowConstraints
+ _OBJC_METACLASS_$__WMCornerRadii
+ _OBJC_METACLASS_$__WMWindowConstraints
+ __OBJC_$_CLASS_METHODS__WMCornerRadii
+ __OBJC_$_CLASS_METHODS__WMWindowConstraints
+ __OBJC_$_CLASS_PROP_LIST__WMCornerRadii
+ __OBJC_$_CLASS_PROP_LIST__WMWindowConstraints
+ __OBJC_$_INSTANCE_METHODS__WMCornerRadii
+ __OBJC_$_INSTANCE_METHODS__WMWindowConstraints
+ __OBJC_$_INSTANCE_VARIABLES__WMCornerRadii
+ __OBJC_$_INSTANCE_VARIABLES__WMWindowConstraints
+ __OBJC_$_PROP_LIST__WMCornerRadii
+ __OBJC_$_PROP_LIST__WMWindowConstraints
+ __OBJC_CLASS_PROTOCOLS_$__WMCornerRadii
+ __OBJC_CLASS_PROTOCOLS_$__WMWindowConstraints
+ __OBJC_CLASS_RO_$__WMCornerRadii
+ __OBJC_CLASS_RO_$__WMWindowConstraints
+ __OBJC_METACLASS_RO_$__WMCornerRadii
+ __OBJC_METACLASS_RO_$__WMWindowConstraints
+ ___28-[_WMWindow setCornerRadii:]_block_invoke
+ ___34-[_WMWindow setWindowConstraints:]_block_invoke
+ ___64-[WMClientWindowManager holdTearOffTabDragWithWindowIdentifier:]_block_invoke
+ ___67-[WMClientWindowManager releaseTearOffTabDragWithWindowIdentifier:]_block_invoke
+ ___76-[WMClientWindowManager refreshTilingConstraintsWithWindowIdentifier:reply:]_block_invoke
+ _objc_msgSend$allocWithZone:
+ _objc_msgSend$clientWindowManager:holdTearOffTabDragForWindowWithIdentifier:
+ _objc_msgSend$clientWindowManager:refreshTilingConstraintsForWindowWithIdentifier:completion:
+ _objc_msgSend$clientWindowManager:releaseTearOffTabDragForWindowWithIdentifier:
+ _objc_msgSend$cornerRadii
+ _objc_msgSend$hash
+ _objc_msgSend$initWithMinSize:maxSize:preferredSize:
+ _objc_msgSend$initWithMinXMinY:maxXMinY:minXMaxY:maxXMaxY:
+ _objc_msgSend$initWithUniformRadius:
+ _objc_msgSend$setCornerRadii:
+ _objc_msgSend$setWindowConstraints:
+ _objc_msgSend$windowConstraints
- GCC_except_table61
- GCC_except_table62
- GCC_except_table79
CStrings:
+ "bl"
+ "br"
+ "cradi"
+ "max"
+ "min"
+ "pref"
+ "tl"
+ "tr"
+ "wcons"
```
