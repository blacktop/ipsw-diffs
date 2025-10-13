## TVRemoteCore

> `/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore`

```diff

-548.10.21.0.0
-  __TEXT.__text: 0x41e34
+548.10.23.0.0
+  __TEXT.__text: 0x41fa0
   __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x59c4
+  __TEXT.__objc_methlist: 0x59dc
   __TEXT.__const: 0x230
   __TEXT.__gcc_except_tab: 0xbec
   __TEXT.__cstring: 0x2ff8
-  __TEXT.__oslogstring: 0x69f6
+  __TEXT.__oslogstring: 0x6a39
   __TEXT.__unwind_info: 0x1000
   __TEXT.__objc_classname: 0x828
-  __TEXT.__objc_methname: 0xc7dc
+  __TEXT.__objc_methname: 0xc820
   __TEXT.__objc_methtype: 0x209c
   __TEXT.__objc_stubs: 0x7f00
   __DATA_CONST.__got: 0x498

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e48
+  __DATA_CONST.__objc_selrefs: 0x2e58
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x128
   __AUTH_CONST.__auth_got: 0x390
   __AUTH_CONST.__const: 0x440
   __AUTH_CONST.__cfstring: 0x3e80
-  __AUTH_CONST.__objc_const: 0x8870
+  __AUTH_CONST.__objc_const: 0x88a0
   __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH.__objc_data: 0x13b0
-  __DATA.__objc_ivar: 0x5ac
+  __DATA.__objc_ivar: 0x5b0
   __DATA.__data: 0x9d0
   __DATA.__bss: 0xf8
   __DATA_DIRTY.__objc_data: 0x140

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 12519EB3-A89F-30AD-B403-3ADFB7249A6D
-  Functions: 1858
-  Symbols:   6327
-  CStrings:  4139
+  UUID: 4DE7197B-B1FD-37DC-B33A-88AA8E6F4F89
+  Functions: 1861
+  Symbols:   6334
+  CStrings:  4143
 
Symbols:
+ -[TVRCRapportRemoteTextInputKeyboardImpl cachedText]
+ -[TVRCRapportRemoteTextInputKeyboardImpl setCachedText:]
+ _OBJC_IVAR_$_TVRCRapportRemoteTextInputKeyboardImpl._cachedText
+ ___53-[TVRCXPCClient deviceQueryUpdatedDiscoveredDevices:]_block_invoke.cold.1
CStrings:
+ "%"
+ "Asking tvremoted to open connection to device %{public}@"
+ "Cached text length:%lu remote text length: %lu"
+ "Keyboard RemoteTextInput source session did begin isEditing: %{bool}d"
+ "Keyboard RemoteTextInput source session did die isEditing: %{bool}d"
+ "Keyboard RemoteTextInput source session did end isEditing: %{bool}d"
+ "T@\"NSString\",C,N,V_cachedText"
+ "_cachedText"
+ "cachedText"
+ "setCachedText:"
- "$"
- "Asking tvremoted to open connection to device %@"
- "Keyboard RemoteTextInput source session did begin"
- "Keyboard RemoteTextInput source session did die"
- "Keyboard RemoteTextInput source session did end"
- "Remote keyboard returning RTI text: length: %lu"

```
