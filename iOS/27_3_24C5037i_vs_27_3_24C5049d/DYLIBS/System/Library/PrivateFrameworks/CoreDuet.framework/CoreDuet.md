## CoreDuet

> `/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet`

```diff

-1977.0.1.0.0
-  __TEXT.__text: 0x189ed8
-  __TEXT.__objc_methlist: 0x11734
-  __TEXT.__cstring: 0x15d8f
-  __TEXT.__const: 0x5d0
-  __TEXT.__oslogstring: 0x18dbb
-  __TEXT.__gcc_except_tab: 0x7408
-  __TEXT.__dlopen_cstrs: 0xb6
-  __TEXT.__unwind_info: 0x6930
+1977.0.2.0.0
+  __TEXT.__text: 0x18aa04
+  __TEXT.__objc_methlist: 0x1177c
+  __TEXT.__cstring: 0x15e09
+  __TEXT.__const: 0x5c0
+  __TEXT.__oslogstring: 0x18e3a
+  __TEXT.__gcc_except_tab: 0x7430
+  __TEXT.__dlopen_cstrs: 0x10e
+  __TEXT.__unwind_info: 0x6970
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3cc0
-  __DATA_CONST.__objc_classlist: 0xc28
+  __DATA_CONST.__const: 0x3d50
+  __DATA_CONST.__objc_classlist: 0xc30
   __DATA_CONST.__objc_catlist: 0x78
-  __DATA_CONST.__objc_protolist: 0x220
+  __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x80a8
+  __DATA_CONST.__objc_selrefs: 0x80e8
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__objc_superrefs: 0x698
+  __DATA_CONST.__objc_superrefs: 0x6a0
   __DATA_CONST.__objc_arraydata: 0x710
-  __DATA_CONST.__got: 0x11a8
+  __DATA_CONST.__got: 0x11b8
   __AUTH_CONST.__const: 0x1b20
-  __AUTH_CONST.__cfstring: 0x12d60
-  __AUTH_CONST.__objc_const: 0x22ec0
+  __AUTH_CONST.__cfstring: 0x12d80
+  __AUTH_CONST.__objc_const: 0x23038
   __AUTH_CONST.__objc_intobj: 0x22c8
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x630
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__auth_got: 0xa80
-  __AUTH.__objc_data: 0x4f38
-  __DATA.__objc_ivar: 0x177c
-  __DATA.__data: 0x1a40
+  __AUTH.__objc_data: 0x4f88
+  __DATA.__objc_ivar: 0x1788
+  __DATA.__data: 0x1aa0
   __DATA.__common: 0x38
   __DATA_DIRTY.__objc_data: 0x2a58
   __DATA_DIRTY.__bss: 0x228

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8794
-  Symbols:   13371
-  CStrings:  4656
+  Functions: 8810
+  Symbols:   13407
+  CStrings:  4664
 
Symbols:
+ +[_CDSiriLearningSettings protectedBundleIDs]
+ -[_CDSiriLearningAppProtectionMonitor .cxx_destruct]
+ -[_CDSiriLearningAppProtectionMonitor appProtectionSubjectsChanged:forSubscription:]
+ -[_CDSiriLearningAppProtectionMonitor initWithHandler:]
+ -[_CDSiriLearningSettings setAppProtectionSubscription:]
+ _AppProtectionLibraryCore
+ _AppProtectionLibraryCore.frameworkLibrary
+ _OBJC_CLASS_$_NSMutableOrderedSet
+ _OBJC_CLASS_$__CDSiriLearningAppProtectionMonitor
+ _OBJC_IVAR_$__CDSiriLearningAppProtectionMonitor._handler
+ _OBJC_IVAR_$__CDSiriLearningSettings._appProtectionSubscription
+ _OBJC_IVAR_$__CDSiriLearningSettings._hasAppProtectionAccess
+ _OBJC_METACLASS_$__CDSiriLearningAppProtectionMonitor
+ __OBJC_$_INSTANCE_METHODS__CDSiriLearningAppProtectionMonitor
+ __OBJC_$_INSTANCE_VARIABLES__CDSiriLearningAppProtectionMonitor
+ __OBJC_$_PROP_LIST__CDSiriLearningAppProtectionMonitor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_APSubjectMonitor
+ __OBJC_$_PROTOCOL_METHOD_TYPES_APSubjectMonitor
+ __OBJC_$_PROTOCOL_REFS_APSubjectMonitor
+ __OBJC_CLASS_PROTOCOLS_$__CDSiriLearningAppProtectionMonitor
+ __OBJC_CLASS_RO_$__CDSiriLearningAppProtectionMonitor
+ __OBJC_LABEL_PROTOCOL_$_APSubjectMonitor
+ __OBJC_METACLASS_RO_$__CDSiriLearningAppProtectionMonitor
+ __OBJC_PROTOCOL_$_APSubjectMonitor
+ ___64-[_CDSiriLearningSettings _startWithCallback:invokeCallbackNow:]_block_invoke_3
+ ___64-[_CDSiriLearningSettings _startWithCallback:invokeCallbackNow:]_block_invoke_4
+ ___AppProtectionLibraryCore_block_invoke
+ ___block_descriptor_40_e8_32bs_e29_v24?0"NSArray"8"NSArray"16ls32l8
+ ___block_descriptor_40_e8_32s_e9_v16?0r*8ls32l8
+ ___block_descriptor_48_e8_32bs_e8_v12?0i8ls32l8
+ ___getAPApplicationClass_block_invoke
+ ___getAPSubjectClass_block_invoke
+ _audit_stringAppProtection
+ _getAPApplicationClass
+ _getAPApplicationClass.softClass
+ _getAPSubjectClass.softClass
CStrings:
+ "APApplication"
+ "APSubject"
+ "AppProtection change"
+ "Unable to read AppProtection (entitled: %{BOOL}d); locked and hidden apps are not excluded from Siri Learning in this process."
+ "com.apple.appprotectiond.read"
+ "com.apple.appprotectiond.read.access"
+ "softlink:o:path:/System/Library/PrivateFrameworks/AppProtection.framework/AppProtection"
+ "v16@?0r*8"
```
