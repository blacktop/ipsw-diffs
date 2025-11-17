## PosterBoardServices

> `/System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices`

```diff

-304.2.5.100.0
-  __TEXT.__text: 0x4a74c
+304.2.6.100.0
+  __TEXT.__text: 0x4b064
   __TEXT.__auth_stubs: 0xaf0
-  __TEXT.__objc_methlist: 0x3b3c
+  __TEXT.__objc_methlist: 0x3c1c
   __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x47a9
+  __TEXT.__cstring: 0x481a
   __TEXT.__gcc_except_tab: 0x90c
   __TEXT.__oslogstring: 0x2867
   __TEXT.__dlopen_cstrs: 0x244
-  __TEXT.__unwind_info: 0x1028
-  __TEXT.__objc_classname: 0x87f
-  __TEXT.__objc_methname: 0xa488
-  __TEXT.__objc_methtype: 0x1b18
-  __TEXT.__objc_stubs: 0x6000
+  __TEXT.__unwind_info: 0x1060
+  __TEXT.__objc_classname: 0x89a
+  __TEXT.__objc_methname: 0xa5f6
+  __TEXT.__objc_methtype: 0x1b71
+  __TEXT.__objc_stubs: 0x60c0
   __DATA_CONST.__got: 0x478
   __DATA_CONST.__const: 0x11c8
-  __DATA_CONST.__objc_classlist: 0x218
+  __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ed0
+  __DATA_CONST.__objc_selrefs: 0x1f08
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x1f0
+  __DATA_CONST.__objc_superrefs: 0x1f8
   __AUTH_CONST.__auth_got: 0x588
   __AUTH_CONST.__const: 0x4c0
-  __AUTH_CONST.__cfstring: 0x36c0
-  __AUTH_CONST.__objc_const: 0xbfe8
+  __AUTH_CONST.__cfstring: 0x3740
+  __AUTH_CONST.__objc_const: 0xc240
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0xaf0
-  __DATA.__objc_ivar: 0x41c
+  __AUTH.__objc_data: 0xb40
+  __DATA.__objc_ivar: 0x42c
   __DATA.__data: 0x5c0
   __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0xa00

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 45970D37-9E69-351D-94C5-620B131B73DE
-  Functions: 1702
-  Symbols:   6039
-  CStrings:  2911
+  UUID: 1B843D39-3D90-3EDA-940B-2425EA7007E9
+  Functions: 1720
+  Symbols:   6103
+  CStrings:  2935
 
Symbols:
+ +[PRSPosterIconConfiguration new]
+ +[PRSPosterIconConfiguration supportsSecureCoding]
+ -[PRSPosterIconConfiguration .cxx_destruct]
+ -[PRSPosterIconConfiguration accentColor]
+ -[PRSPosterIconConfiguration description]
+ -[PRSPosterIconConfiguration encodeWithCoder:]
+ -[PRSPosterIconConfiguration hash]
+ -[PRSPosterIconConfiguration initWithCoder:]
+ -[PRSPosterIconConfiguration initWithPoster:type:variant:accentColor:]
+ -[PRSPosterIconConfiguration init]
+ -[PRSPosterIconConfiguration isEqualToPosterIconConfiguration:]
+ -[PRSPosterIconConfiguration posterConfiguration]
+ -[PRSPosterIconConfiguration type]
+ -[PRSPosterIconConfiguration variant]
+ -[PRSServer fetchLockScreenHomeScreenColorConfigurations:]
+ -[PRSService fetchLockScreenHomeScreenColorConfigurations:]
+ -[PRSService fetchLockScreenHomeScreenColorConfigurations:].cold.1
+ _OBJC_CLASS_$_PRSPosterIconConfiguration
+ _OBJC_IVAR_$_PRSPosterIconConfiguration._accentColor
+ _OBJC_IVAR_$_PRSPosterIconConfiguration._posterConfiguration
+ _OBJC_IVAR_$_PRSPosterIconConfiguration._type
+ _OBJC_IVAR_$_PRSPosterIconConfiguration._variant
+ _OBJC_METACLASS_$_PRSPosterIconConfiguration
+ __OBJC_$_CLASS_METHODS_PRSPosterIconConfiguration
+ __OBJC_$_CLASS_PROP_LIST_PRSPosterIconConfiguration
+ __OBJC_$_INSTANCE_METHODS_PRSPosterIconConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_PRSPosterIconConfiguration
+ __OBJC_$_PROP_LIST_PRSPosterIconConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_PRSPosterIconConfiguration
+ __OBJC_CLASS_RO_$_PRSPosterIconConfiguration
+ __OBJC_METACLASS_RO_$_PRSPosterIconConfiguration
+ ___59-[PRSService fetchLockScreenHomeScreenColorConfigurations:]_block_invoke
+ ___59-[PRSService fetchLockScreenHomeScreenColorConfigurations:]_block_invoke.cold.1
+ _objc_msgSend$accentColor
+ _objc_msgSend$doesNotRecognizeSelector:
+ _objc_msgSend$fetchLockScreenHomeScreenColorConfigurations:
+ _objc_msgSend$initWithPoster:type:variant:accentColor:
+ _objc_msgSend$posterConfiguration
+ _objc_msgSend$server:fetchLockScreenHomeScreenColorConfigurations:
CStrings:
+ "-[PRSServer fetchLockScreenHomeScreenColorConfigurations:]"
+ "@48@0:8@16Q24Q32@40"
+ "PRSPosterIconConfiguration"
+ "T@\"BSColor\",R,N,V_accentColor"
+ "T@\"PRSPosterConfiguration\",R,N,V_posterConfiguration"
+ "TQ,R,N,V_variant"
+ "_accentColor"
+ "_posterConfiguration"
+ "accentColor"
+ "doesNotRecognizeSelector:"
+ "fetchLockScreenHomeScreenColorConfigurations:"
+ "initWithPoster:type:variant:accentColor:"
+ "isEqualToPosterIconConfiguration:"
+ "posterConfiguration"
+ "server:fetchLockScreenHomeScreenColorConfigurations:"
+ "v24@0:8@?<v@?@\"NSArray<__PRSPosterIconConfiguration__>\"@\"NSError\">16"

```
