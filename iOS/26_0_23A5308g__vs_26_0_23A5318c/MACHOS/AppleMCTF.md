## AppleMCTF

> `/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF`

```diff

-904.72.0.0.0
-  __TEXT.__text: 0x74d10
+904.76.7.0.0
+  __TEXT.__text: 0x75a3c
   __TEXT.__auth_stubs: 0xd40
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0x4
   __TEXT.__gcc_except_tab: 0x63c
-  __TEXT.__cstring: 0x2313c
-  __TEXT.__const: 0x1e768
+  __TEXT.__cstring: 0x23475
+  __TEXT.__const: 0x1eaf8
   __TEXT.__objc_methname: 0xb
   __TEXT.__unwind_info: 0x608
   __DATA_CONST.__auth_got: 0x6b0

   __DATA_CONST.__cfstring: 0x480
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x8
-  __DATA.__data: 0xe0
-  __DATA.__bss: 0x858
+  __DATA.__data: 0x100
+  __DATA.__bss: 0x860
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 38F61798-5FB4-37C6-9BFD-A28588666387
-  Functions: 612
+  UUID: 5BAD4C15-D64F-30D1-AAF6-D7331E7776BF
+  Functions: 613
   Symbols:   354
-  CStrings:  2959
+  CStrings:  2976
 
CStrings:
+ "%lld %d AVE %s: %s:%d %s | wrong Crypto info %p %d"
+ "%lld %d AVE %s: %s:%d %s | wrong Crypto info %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %p %lld Frame %d add RPU nut %p %d"
+ "%lld %d AVE %s: %s::%s:%d %p %lld Frame %d add RPU nut %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %p %lld Frame %d add RPU nut in crypto info %p %ld %d"
+ "%lld %d AVE %s: %s::%s:%d %p %lld Frame %d add RPU nut in crypto info %p %ld %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | %p %lld add RPU crypto info failed frame %d %ld %p"
+ "%lld %d AVE %s: %s::%s:%d %s | %p %lld add RPU crypto info failed frame %d %ld %p\n"
+ "%lld %d AVE %s: Crypto %s size %d"
+ "%lld %d AVE %s: Crypto %s size %d\n"
+ "%lld %d AVE %s: Crypto %s | %d %d"
+ "%lld %d AVE %s: Crypto %s | %d %d\n"
+ "(0 <= psInfo->iNum) && (psInfo->iNum < (((2) < ((63 + 1)) ? (2) : ((63 + 1))) * ((32) < (256) ? (32) : (256)) + 1))"
+ "(0 <= psInfo->iNum) && (psInfo->iNum <= (((2) < ((63 + 1)) ? (2) : ((63 + 1))) * ((32) < (256) ? (32) : (256)) + 1))"
+ "(iOffset >= 0) && (iSize >= 0) && (psInfo != __null)"
+ "21:01:09"
+ "904.76.7"
+ "AVE_Crypto_PrintInfo"
+ "AVE_MCTFRampUpFrameNum"
+ "Aug  7 2025"
+ "Crypto %s size %d"
+ "Crypto %s size %d\n"
+ "Crypto %s | %d %d"
+ "Crypto %s | %d %d\n"
- "%lld %d AVE %s: %s::%s:%d %p %lld add RPU nut %p %d"
- "%lld %d AVE %s: %s::%s:%d %p %lld add RPU nut %p %d\n"
- "(0 <= psInfo->iNum) && (psInfo->iNum < (((2) < ((63 + 1)) ? (2) : ((63 + 1))) * ((32) < (256) ? (32) : (256))))"
- "(iOffset >= 0) && (iSize > 0) && (psInfo != __null)"
- "22:24:14"
- "904.72.0"
- "Jul 25 2025"

```
