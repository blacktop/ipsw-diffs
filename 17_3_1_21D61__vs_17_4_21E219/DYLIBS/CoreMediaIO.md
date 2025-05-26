## CoreMediaIO

> `/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO`

```diff

-5518.3.0.0.0
-  __TEXT.__text: 0x43efc
+5522.10.1.0.0
+  __TEXT.__text: 0x44ecc
   __TEXT.__auth_stubs: 0xdd0
-  __TEXT.__objc_methlist: 0x1bf4
+  __TEXT.__objc_methlist: 0x1c1c
   __TEXT.__const: 0x7c
   __TEXT.__gcc_except_tab: 0x126c
-  __TEXT.__cstring: 0x80d9
-  __TEXT.__oslogstring: 0x3d49
+  __TEXT.__cstring: 0x8218
+  __TEXT.__oslogstring: 0x4024
   __TEXT.__dlopen_cstrs: 0xb8
-  __TEXT.__unwind_info: 0xbc4
+  __TEXT.__unwind_info: 0xbcc
   __TEXT.__objc_classname: 0x395
-  __TEXT.__objc_methname: 0x4b16
+  __TEXT.__objc_methname: 0x4b62
   __TEXT.__objc_methtype: 0x10e4
-  __TEXT.__objc_stubs: 0x2fc0
+  __TEXT.__objc_stubs: 0x3020
   __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0xd18
+  __DATA_CONST.__const: 0xd28
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x3148
-  __DATA_CONST.__objc_selrefs: 0xee8
-  __AUTH_CONST.__cfstring: 0x1dc0
-  __AUTH_CONST.__const: 0xc0
+  __DATA_CONST.__objc_selrefs: 0xf08
+  __DATA_CONST.__objc_classrefs: 0x150
+  __DATA_CONST.__objc_superrefs: 0xd0
+  __AUTH_CONST.__cfstring: 0x1e00
+  __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__auth_got: 0x6f8
-  __DATA.__objc_classrefs: 0x150
-  __DATA.__objc_superrefs: 0xd0
   __DATA.__objc_ivar: 0x354
-  __DATA.__data: 0x4b8
-  __DATA.__bss: 0x70
-  __DATA.__common: 0x15
-  __DATA_DIRTY.__const: 0x280
+  __DATA.__data: 0x4b0
+  __DATA.__bss: 0x60
+  __DATA_DIRTY.__const: 0x220
   __DATA_DIRTY.__objc_const: 0xdc8
   __DATA_DIRTY.__objc_data: 0x820
-  __DATA_DIRTY.__bss: 0xdc
+  __DATA_DIRTY.__bss: 0xfc
+  __DATA_DIRTY.__common: 0x1d
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1343
-  Symbols:   4097
-  CStrings:  1880
+  Functions: 1345
+  Symbols:   4107
+  CStrings:  1908
 
Symbols:
+ +[CMIOExtensionProvider stopServiceWithProvider:]
+ -[CMIOExtensionProvider removeAllProviderContexts]
+ -[CMIOExtensionProviderServer stop]
+ GCC_except_table148
+ GCC_except_table156
+ GCC_except_table160
+ GCC_except_table165
+ GCC_except_table170
+ GCC_except_table179
+ GCC_except_table186
+ GCC_except_table193
+ GCC_except_table198
+ GCC_except_table201
+ GCC_except_table207
+ GCC_except_table210
+ _CMIOExtensionPropertyDeviceLatency
+ _CMIOExtensionPropertyStreamLatency
+ ___block_literal_global.150
+ ___block_literal_global.195
+ ___block_literal_global.379
+ _gProviderLock
+ _objc_msgSend$removeAllProviderContexts
+ _objc_msgSend$retainCount
+ _objc_msgSend$stop
- GCC_except_table152
- GCC_except_table158
- GCC_except_table163
- GCC_except_table164
- GCC_except_table173
- GCC_except_table182
- GCC_except_table191
- GCC_except_table194
- GCC_except_table199
- GCC_except_table205
- GCC_except_table208
- ___block_literal_global.149
- ___block_literal_global.194
- ___block_literal_global.378
CStrings:
+ "%s:%d:%s %@: cancelling listener"
+ "%s:%d:%s %@: finished stopping things"
+ "%s:%d:%s %p (%@), autoreleased global provider %p (its retain count is %d)"
+ "%s:%d:%s %p, autoreleased global provider %p (its retain count is %d)"
+ "%s:%d:%s CMIOExtensionProvider.sharedProvider = %@"
+ "%s:%d:%s Retained and set gProvider to %p (retain count %d)"
+ "%s:%d:%s SetProperty - %@"
+ "%s:%d:%s calling [super dealloc]"
+ "%s:%d:%s dealloc done"
+ "%s:%d:%s dealloc starting"
+ "%s:%d:%s dealloc starting, shared provider reference %p"
+ "%s:%d:%s leaving"
+ "%s:%d:%s released and set shared provider reference to nil"
+ "%s:%d:%s releasing shared provider reference %p (its retain count is %d)"
+ "%s:%d:%s removing all contexts from %@"
+ "%s:%d:%s returning autoreleased global provider %p (its retain count is %d)"
+ "%s:%d:%s shared server %@ has been stopped"
+ "%s:%d:%s stopping shared server %@"
+ "+[CMIOExtensionProvider sharedProvider]"
+ "+[CMIOExtensionProvider stopServiceWithProvider:]"
+ "-[CMIOExtensionProvider dealloc]"
+ "-[CMIOExtensionProvider removeAllProviderContexts]"
+ "-[CMIOExtensionProviderServer dealloc]"
+ "-[CMIOExtensionProviderServer stop]"
+ "CMIOExtensionPropertyDeviceLatency"
+ "CMIOExtensionPropertyStreamLatency"
+ "T@\"NSString\",?,R,C"
+ "removeAllProviderContexts"
+ "stop"
+ "stopServiceWithProvider:"
- "%s:%d:%s setting global provider to %p"
- "%s:%d:%s startServiceWithProvider:%p (%@), global provider %p"

```
