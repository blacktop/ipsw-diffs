## AppleMCTF

> `/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF`

```diff

-703.54.1.0.0
-  __TEXT.__text: 0xe9760
+760.23.1.0.0
+  __TEXT.__text: 0xea9f0
   __TEXT.__auth_stubs: 0xeb0
   __TEXT.__init_offsets: 0x8
-  __TEXT.__cstring: 0x640c5
+  __TEXT.__cstring: 0x647d0
   __TEXT.__const: 0x107a8
   __TEXT.__gcc_except_tab: 0x1fc
-  __TEXT.__unwind_info: 0x76c
+  __TEXT.__unwind_info: 0x790
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x760
-  __DATA_CONST.__got: 0x8a8
+  __DATA_CONST.__got: 0x8b0
   __DATA_CONST.__auth_ptr: 0x30
   __DATA_CONST.__const: 0x2300
-  __DATA_CONST.__cfstring: 0x23c0
+  __DATA_CONST.__cfstring: 0x23e0
   __DATA.__data: 0x20
   __DATA.__bss: 0x5d0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/OpticalFlowFramework.framework/OpticalFlowFramework
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 02DB813A-0D02-3515-9C7B-BD0DC9F2DA97
-  Functions: 622
-  Symbols:   561
-  CStrings:  6555
+  UUID: DB69C18C-DD00-3087-8791-4D536F50A1A8
+  Functions: 629
+  Symbols:   562
+  CStrings:  6582
 
Symbols:
+ _kVTTemporalFilterPropertyKey_FilterStrength
CStrings:
+ "%lld %d AVE %s: %s eMCTFMode = %d"
+ "%lld %d AVE %s: %s eMCTFMode = %d\n"
+ "%lld %d AVE %s: %s:%d %s | AVE MCTF: (CFGNumberetTypeID) failed"
+ "%lld %d AVE %s: %s:%d %s | AVE MCTF: (CFGNumberetTypeID) failed\n"
+ "%lld %d AVE %s: AVE FIG WARNING: MCTF mode = %d is set."
+ "%lld %d AVE %s: AVE FIG WARNING: MCTF mode = %d is set.\n"
+ "%lld %d AVE %s: F %d bGap %d Send Complete command to close GOP"
+ "%lld %d AVE %s: F %d bGap %d Send Complete command to close GOP\n"
+ "%lld %d AVE %s: FIG: asked for AVE_kVTEncodeFrameOptionKey_MCTFMode return %d"
+ "%lld %d AVE %s: FIG: asked for AVE_kVTEncodeFrameOptionKey_MCTFMode return %d\n"
+ "%lld %d AVE %s: FIG: iMCTFMode = %u"
+ "%lld %d AVE %s: FIG: iMCTFMode = %u\n"
+ "%lld %d AVE %s: FIG: received ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"MCTFMode\" \"\"))"
+ "%lld %d AVE %s: FIG: received ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"MCTFMode\" \"\"))\n"
+ "%lld %d AVE %s: FIG: received AVE_kVTCompressionPropertyKey_MCTFParams"
+ "%lld %d AVE %s: FIG: received AVE_kVTCompressionPropertyKey_MCTFParams\n"
+ "%lld %d AVE %s: MCTF %s | %p %d | %d %d %d - %d %d %d - %d %d %d %d %d %d %d %d %d"
+ "%lld %d AVE %s: MCTF %s | %p %d | %d %d %d - %d %d %d - %d %d %d %d %d %d %d %d %d\n"
+ "%lld %d AVE %s: MCTF Params: %d | %d %d %d - %d %d %d - %d %d %d %d %d %d %d %d %d"
+ "%lld %d AVE %s: MCTF Params: %d | %d %d %d - %d %d %d - %d %d %d %d %d %d %d %d %d\n"
+ "%lld %d AVE %s: MCTF Pop [%d]: %d | %d %d %d - %d %d %d - %d %d %d %d %d %d %d %d %d"
+ "%lld %d AVE %s: MCTF Pop [%d]: %d | %d %d %d - %d %d %d - %d %d %d %d %d %d %d %d %d\n"
+ "AVE_AddSupportedProperty(PropertyDictionary, kVTPropertyType_Boolean, ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"MCTFMode\" \"\")), false)"
+ "AVE_AddSupportedProperty(PropertyDictionaryHEIF, kVTPropertyType_Boolean, ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"CalculateMeanSquaredError\" \"\")), false)"
+ "AVE_MCTF_Retrieve"
+ "CFNumberGetTypeID() == CFGetTypeID(pValue)"
+ "MCTF %s | %p %d | %d %d %d - %d %d %d - %d %d %d %d %d %d %d %d %d"
+ "MCTF %s | %p %d | %d %d %d - %d %d %d - %d %d %d %d %d %d %d %d %d\n"
+ "MCTFMode"
+ "MCTFParams"
+ "pArray != __null && pMCTF != __null"
- "%lld %d AVE %s: %s:%d: %d ForceKeyFrame IDR without COMPLETE MiniGOP"
- "%lld %d AVE %s: %s:%d: %d ForceKeyFrame IDR without COMPLETE MiniGOP\n"
- "%lld %d AVE %s: F %d bGap %d Force %d Send Complete command to close GOP"
- "%lld %d AVE %s: F %d bGap %d Force %d Send Complete command to close GOP\n"
- "FilterStrength"

```
