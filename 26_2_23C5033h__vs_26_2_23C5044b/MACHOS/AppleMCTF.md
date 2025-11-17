## AppleMCTF

> `/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF`

```diff

-905.5.3.0.0
-  __TEXT.__text: 0x76280
-  __TEXT.__auth_stubs: 0xd40
+905.17.4.0.0
+  __TEXT.__text: 0x772f0
+  __TEXT.__auth_stubs: 0xd50
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0x4
   __TEXT.__gcc_except_tab: 0x63c
-  __TEXT.__cstring: 0x2389b
-  __TEXT.__const: 0x1f3a8
+  __TEXT.__cstring: 0x23a6b
+  __TEXT.__const: 0x1fa68
   __TEXT.__objc_methname: 0xb
   __TEXT.__unwind_info: 0x610
-  __DATA_CONST.__auth_got: 0x6b0
+  __DATA_CONST.__auth_got: 0x6b8
   __DATA_CONST.__got: 0x438
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x41b0
-  __DATA_CONST.__cfstring: 0x480
+  __DATA_CONST.__const: 0x4230
+  __DATA_CONST.__cfstring: 0x500
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x8
   __DATA.__data: 0x198
-  __DATA.__bss: 0x910
+  __DATA.__bss: 0x9d0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7E8FEA91-6104-3322-8566-448A25A25794
-  Functions: 619
-  Symbols:   354
-  CStrings:  2991
+  UUID: D5A1E47B-EF47-3A72-B8AF-F10D7998EA9B
+  Functions: 623
+  Symbols:   355
+  CStrings:  3008
 
Symbols:
+ _CVBufferSetAttachment
CStrings:
+ "%lld %d AVE %s: %s:%d  [%d] pMCTF = %p %lld, output CVPixelFormatType = %d %lu x %lu, Strength = %d"
+ "%lld %d AVE %s: %s:%d  [%d] pMCTF = %p %lld, output CVPixelFormatType = %d %lu x %lu, Strength = %d\n"
+ "%lld %d AVE %s: %s:%d %s | fail to create CFNumber for %p strength %d"
+ "%lld %d AVE %s: %s:%d %s | fail to create CFNumber for %p strength %d\n"
+ "%lld %d AVE %s: %s:%d %s | fail to create pMctfAttachment for %p"
+ "%lld %d AVE %s: %s:%d %s | fail to create pMctfAttachment for %p\n"
+ "%lld %d AVE %s: %s:%d %s | out of range %p %lld %p %p %p %d"
+ "%lld %d AVE %s: %s:%d %s | out of range %p %lld %p %p %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d encoding error %d %d %d %d"
+ "%lld %d AVE %s: %s::%s:%d encoding error %d %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d frame drop %lld %d %lld %d %d 0x%x %p"
+ "%lld %d AVE %s: %s::%s:%d frame drop %lld %d %lld %d %d 0x%x %p\n"
+ "%lld %d AVE %s: UserQpMapSize (%d) does not match required size (%d), disabling userQPMap feature"
+ "%lld %d AVE %s: UserQpMapSize (%d) does not match required size (%d), disabling userQPMap feature\n"
+ "21:51:08"
+ "905.17.4"
+ "AVE_Prop_MCTF_GetLRMEFSLambdaLinear"
+ "AVE_Prop_MCTF_GetLRMEFSMVCostMode"
+ "AVE_Prop_MCTF_SetLRMEFSLambdaLinear"
+ "AVE_Prop_MCTF_SetLRMEFSMVCostMode"
+ "AVE_kVTCompressionPropertyKey_LRMEFSLambdaLinear"
+ "AVE_kVTCompressionPropertyKey_LRMEFSMVCostMode"
+ "LRMEFSLambdaLinear"
+ "LRMEFSMVCostMode"
+ "Nov 12 2025"
+ "StrengthLevel"
+ "iLinear >= 0"
+ "iMode >= 0"
+ "pMctfAttachment != __null"
- "%lld %d AVE %s: \nH264FrameRec: counter received = %d"
- "%lld %d AVE %s: \nH264FrameRec: counter received = %d\n"
- "%lld %d AVE %s: %s:%d %s | H264FrameRec ERROR: commandResult != kIOReturnSuccess."
- "%lld %d AVE %s: %s:%d %s | H264FrameRec ERROR: commandResult != kIOReturnSuccess.\n"
- "%lld %d AVE %s: %s:%d: pMCTF = %p %lld, output CVPixelFormatType = %d %lu x %lu"
- "%lld %d AVE %s: %s:%d: pMCTF = %p %lld, output CVPixelFormatType = %d %lu x %lu\n"
- "%lld %d AVE %s: %s::%s:%d frame drop %lld %d %lld %d 0x%x %p"
- "%lld %d AVE %s: %s::%s:%d frame drop %lld %d %lld %d 0x%x %p\n"
- "%lld %d AVE %s: FIG: H264FrameRec: commandResult = kIOReturnNoResources"
- "%lld %d AVE %s: FIG: H264FrameRec: commandResult = kIOReturnNoResources\n"
- "%lld %d AVE %s: UserQpMapSize (%d) is smaller than required (%d), copying only received data"
- "%lld %d AVE %s: UserQpMapSize (%d) is smaller than required (%d), copying only received data\n"
- "20:55:44"
- "905.5.3"
- "Nov  3 2025"
- "result == 0"

```
