## AppleServiceToolkit

> `/System/Library/PrivateFrameworks/AppleServiceToolkit.framework/AppleServiceToolkit`

```diff

-128.1.3.0.0
-  __TEXT.__text: 0x1d634
+128.2.0.0.0
+  __TEXT.__text: 0x1dc7c
   __TEXT.__auth_stubs: 0x700
   __TEXT.__objc_methlist: 0x20c0
   __TEXT.__const: 0x108
-  __TEXT.__cstring: 0x186c
-  __TEXT.__oslogstring: 0x11e3
+  __TEXT.__cstring: 0x1990
+  __TEXT.__oslogstring: 0x124b
   __TEXT.__gcc_except_tab: 0xa54
-  __TEXT.__unwind_info: 0x8fc
-  __TEXT.__objc_classname: 0x515
-  __TEXT.__objc_methname: 0x5730
+  __TEXT.__unwind_info: 0x90c
+  __TEXT.__objc_classname: 0x513
+  __TEXT.__objc_methname: 0x5716
   __TEXT.__objc_methtype: 0x13d6
   __TEXT.__objc_stubs: 0x4760
   __DATA_CONST.__got: 0x68

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3fb0
+  __DATA_CONST.__objc_const: 0x3f90
   __DATA_CONST.__objc_selrefs: 0x1518
   __DATA_CONST.__objc_arraydata: 0xf8
   __AUTH_CONST.__cfstring: 0x2120

   __DATA.__objc_protorefs: 0x20
   __DATA.__objc_classrefs: 0x230
   __DATA.__objc_superrefs: 0x118
-  __DATA.__objc_ivar: 0x28c
+  __DATA.__objc_ivar: 0x288
   __DATA.__data: 0x6d0
-  __DATA.__bss: 0x148
+  __DATA.__bss: 0x150
   __DATA_DIRTY.__objc_data: 0x168
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: C7B286FA-C817-3ED7-9749-89D8EE3F45FE
+  UUID: D281C02B-2C0D-35A2-BD9A-0CF077872BDB
   Functions: 844
   Symbols:   3228
-  CStrings:  1957
+  CStrings:  1967
 
Symbols:
+ _ASTCurrentDiagsChannel
- _OBJC_IVAR_$_ASTEnvironment._diagsChannel
CStrings:
+ "+[ASTEnvironment currentEnvironment]"
+ "+[ASTEnvironment environmentWithEnvironmentType:]"
+ "-[ASTEnvironment _generateServerURL]"
+ "-[ASTEnvironment initWithEnvironmentType:]"
+ "-[ASTEnvironment init]"
+ "-[ASTEnvironment setDiagsChannel:]"
+ "-[ASTEnvironment setEnvironmentType:]"
+ "-[ASTEnvironment setServer:]"
+ "T@\"NSString\",&,N"
+ "[%@] %s"
+ "[%@] New server URL: %@"
+ "[%@] Updating diags channel to: %@"
+ "[Session] Received diags channel: %@"
- "$"
- "T@\"NSString\",&,N,V_diagsChannel"
- "_diagsChannel"

```
