## CoreMedia

> `/System/Library/Frameworks/CoreMedia.framework/CoreMedia`

```diff

-3255.61.4.11.7
-  __TEXT.__text: 0x28a130
-  __TEXT.__auth_stubs: 0x34f0
+3255.66.6.11.2
+  __TEXT.__text: 0x28a6c8
+  __TEXT.__auth_stubs: 0x3510
   __TEXT.__objc_methlist: 0x53c
   __TEXT.__const: 0x1ba0
-  __TEXT.__oslogstring: 0x2d775
-  __TEXT.__cstring: 0x584eb
+  __TEXT.__oslogstring: 0x2d852
+  __TEXT.__cstring: 0x585b9
   __TEXT.__gcc_except_tab: 0x1b8
   __TEXT.__dlopen_cstrs: 0x190
   __TEXT.__unwind_info: 0x4f68

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0xd8
-  __AUTH_CONST.__auth_got: 0x1a88
+  __AUTH_CONST.__auth_got: 0x1a98
   __AUTH_CONST.__const: 0x6120
-  __AUTH_CONST.__cfstring: 0x17f80
+  __AUTH_CONST.__cfstring: 0x17fa0
   __AUTH_CONST.__objc_const: 0xb20
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x78

   __DATA.__data: 0xa51
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x800
-  __DATA.__bss: 0x1400
+  __DATA.__bss: 0x13f8
   __DATA_DIRTY.__data: 0x2fc
   __DATA_DIRTY.__common: 0x298
-  __DATA_DIRTY.__bss: 0x1878
+  __DATA_DIRTY.__bss: 0x1890
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: B8B01339-0CEC-3A5D-A7AD-F8DEEED8414D
-  Functions: 10781
-  Symbols:   26314
-  CStrings:  17309
+  UUID: 4D5B6700-EBE8-3E50-AC61-8626F9709232
+  Functions: 10786
+  Symbols:   26320
+  CStrings:  17319
 
Symbols:
+ _CFAllocatorCreateWithZone
+ _FigVideoFormatDescriptionCopyVEXUExtensions
+ _darwinMemory_createCustomAllocator
+ _sandbox_check
- _CM8021ASClockEnsureTimeSyncServices.cold.1
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/CoreMedia_CoreMedia/Sources/Utilities/FigDispatchUtilities.c %s: sandbox check for creating dispatch workloop failed"
+ "<<<< 8021ASClock >>>> %s: Added gPTP TimeSync Services"
+ "<<<< FigNetworkHistory >>>> %s:  %p: requestID: %lx at %.3f numBytes: %lld rtt_ms: %d"
+ "CFAllocatorCreateWithZone"
+ "FigVideoFormatDescriptionCopyVEXUExtensions"
+ "UseDispatchWorkloopForAsyncPlayer"
+ "audiomxd triage"
+ "figDispatch_shouldUseWorkloopForFigThreadPriority"
+ "syscall-unix"
+ "vexuExtensions is NULL"
- "<<<< FigNetworkHistory >>>> %s:  %p: requestID: %lx at %.3f numBytes: %lld"

```
