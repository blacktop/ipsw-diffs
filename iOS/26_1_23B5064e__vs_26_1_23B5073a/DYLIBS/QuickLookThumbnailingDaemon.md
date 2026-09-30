## QuickLookThumbnailingDaemon

> `/System/Library/PrivateFrameworks/QuickLookThumbnailingDaemon.framework/QuickLookThumbnailingDaemon`

```diff

-208.1.3.0.0
-  __TEXT.__text: 0x5597c
+208.1.4.0.0
+  __TEXT.__text: 0x55ec4
   __TEXT.__auth_stubs: 0x1f10
-  __TEXT.__objc_methlist: 0x31ac
-  __TEXT.__const: 0xe74
+  __TEXT.__objc_methlist: 0x31c4
+  __TEXT.__const: 0x1054
   __TEXT.__gcc_except_tab: 0xe58
   __TEXT.__cstring: 0x475b
   __TEXT.__oslogstring: 0x52c6

   __TEXT.__unwind_info: 0x14b0
   __TEXT.__eh_frame: 0x6a8
   __TEXT.__objc_classname: 0x501
-  __TEXT.__objc_methname: 0x9c4e
+  __TEXT.__objc_methname: 0x9ce8
   __TEXT.__objc_methtype: 0x1b0d
   __TEXT.__objc_stubs: 0x7600
   __DATA_CONST.__got: 0x750

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2498
+  __DATA_CONST.__objc_selrefs: 0x24a8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xf0
   __AUTH_CONST.__auth_got: 0xf98
   __AUTH_CONST.__const: 0x9a0
   __AUTH_CONST.__cfstring: 0x1bc0
-  __AUTH_CONST.__objc_const: 0x5258
+  __AUTH_CONST.__objc_const: 0x52b8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x2e0
   __AUTH.__data: 0xf0
-  __DATA.__objc_ivar: 0x478
-  __DATA.__data: 0x620
+  __DATA.__objc_ivar: 0x480
+  __DATA.__data: 0x720
   __DATA.__bss: 0xe50
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0xc88
-  __DATA_DIRTY.__data: 0x368
+  __DATA_DIRTY.__data: 0x278
   __DATA_DIRTY.__bss: 0x290
   __DATA_DIRTY.__common: 0x80
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9B1AC7C4-6D39-383B-98F4-289CB334D563
-  Functions: 2014
-  Symbols:   5823
-  CStrings:  3016
+  UUID: 5772CB80-9D2D-30D5-B79D-13D2EB189349
+  Functions: 2016
+  Symbols:   5829
+  CStrings:  3022
 
Symbols:
+ -[QLServerThread domainCacheLock]
+ -[QLServerThread fsidCacheLock]
+ -[QLServerThread volumeCacheLock]
+ _OBJC_IVAR_$_QLServerThread._domainCacheLock
+ _OBJC_IVAR_$_QLServerThread._fsidCacheLock
+ _OBJC_IVAR_$_QLServerThread._volumeCacheLock
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_instantiateConcreteTypeFromMangledNameV2
- -[QLServerThread cacheInitLock]
- _OBJC_IVAR_$_QLServerThread._cacheInitLock
- ___swift_instantiateConcreteTypeFromMangledName
- ___swift_instantiateConcreteTypeFromMangledNameAbstract
CStrings:
+ "T{os_unfair_lock_s=I},R,N,V_domainCacheLock"
+ "T{os_unfair_lock_s=I},R,N,V_fsidCacheLock"
+ "T{os_unfair_lock_s=I},R,N,V_volumeCacheLock"
+ "_domainCacheLock"
+ "_fsidCacheLock"
+ "_volumeCacheLock"
+ "domainCacheLock"
+ "fsidCacheLock"
+ "volumeCacheLock"
- "T{os_unfair_lock_s=I},R,N,V_cacheInitLock"
- "_cacheInitLock"
- "cacheInitLock"

```
