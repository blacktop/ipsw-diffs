## libhwtrace.dylib

> `/usr/lib/libhwtrace.dylib`

```diff

-133.0.2.0.0
-  __TEXT.__text: 0x2211cc
+133.0.14.0.0
+  __TEXT.__text: 0x21accc
   __TEXT.__auth_stubs: 0x1690
-  __TEXT.__const: 0x1adf40
-  __TEXT.__cstring: 0x19769
+  __TEXT.__const: 0x1ae020
+  __TEXT.__cstring: 0x1995c
   __TEXT.__oslogstring: 0x6b0
-  __TEXT.__gcc_except_tab: 0x25c
-  __TEXT.__unwind_info: 0x2160
-  __TEXT.__eh_frame: 0xe0
+  __TEXT.__gcc_except_tab: 0x290
+  __TEXT.__unwind_info: 0x2b90
+  __TEXT.__eh_frame: 0x98
   __TEXT.__objc_methname: 0xa9
   __TEXT.__objc_stubs: 0x120
   __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x48a20
+  __DATA_CONST.__const: 0x48af8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x48
   __AUTH_CONST.__auth_got: 0xb58
-  __AUTH_CONST.__const: 0x6598
+  __AUTH_CONST.__const: 0x6618
   __AUTH_CONST.__cfstring: 0x320
   __AUTH.__data: 0x18
   __DATA.__data: 0x68
-  __DATA.__bss: 0x508
-  __DATA.__common: 0x6e0
+  __DATA.__bss: 0xa78
+  __DATA.__common: 0x16b
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libncurses.5.4.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: CF9870D5-AE55-330A-AB90-924A62DAD4A8
-  Functions: 3416
+  UUID: BB646619-7580-361C-A417-FC09227ADC3B
+  Functions: 4324
   Symbols:   573
-  CStrings:  5641
+  CStrings:  5701
 
Symbols:
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEPKcm
- _objc_release
CStrings:
+ " \t\n\v\f\r"
+ " is present but its filename is unknown: consider passing it in via the `apple-hwtrace record -image=...` argument. If using `trace record`, see 111873589 for a workaround."
+ "+cpuhelp"
+ "+help"
+ ", asid="
+ ". note: H12 devices like (e.g. iPhone 11 variants) aren't supported due to 55118318."
+ "0b"
+ "0o"
+ "ContextSwitchIgnoreAddressSpaceSwitch"
+ "Expected exactly 1 process ID to trace"
+ "Failed to parse version info: "
+ "Legacy xnu-based streaming-to-DRAM no longer supported (150685905), use --CPUTrace:driver=1"
+ "Multiple shared caches are unsupported (106054931): tracking "
+ "Must specify process ID to configure a Production Trace"
+ "This happened because the device is not provisioned to record a Processor Trace."
+ "Unsupported minor format version"
+ "X"
+ "X+"
+ "X-"
+ "__rtk_mmu_gxf_dispatcher_entry"
+ "` in your `apple-hwtrace record ...` invocation to fix this. If using `trace record`, see 111873589 for a workaround."
+ "amd64"
+ "arm64ec"
+ "i786"
+ "i886"
+ "i986"
+ "libhwtrace @ tag libhwtrace-133.0.14"
+ "libhwtrace @ tag libhwtrace-133.0.14\n"
+ "mips64eb"
+ "mips64r6"
+ "mipsallegrex"
+ "mipsallegrexel"
+ "mipseb"
+ "mipsisa32r6"
+ "mipsisa32r6el"
+ "mipsisa64r6"
+ "mipsisa64r6el"
+ "mipsn32"
+ "mipsn32el"
+ "mipsn32r6"
+ "mipsr6"
+ "mipsr6el"
+ "powerpcspe"
+ "ppc32"
+ "ppc32le"
+ "ppcle"
+ "ppu"
+ "sparc64"
+ "spirv1.5"
+ "spirv1.6"
+ "systemz"
+ "v6sm"
+ "v7a"
+ "v7em"
+ "v7hl"
+ "v7l"
+ "v7m"
+ "v7r"
+ "v8"
+ "v8.1m.main"
+ "v8l"
+ "v8m.base"
+ "v8m.main"
+ "v9"
+ "x"
+ "x+"
+ "x-"
+ "xscaleeb"
+ "{}"
- " is present but its filename is unknown: consider passing it in via the `apple-hwtrace record -image=...` argument. If using `trace record`, see rdar://111873589 for a workaround."
- ". note: H12 devices like (e.g. iPhone 11 variants) aren't supported due to rdar://55118318."
- "Legacy xnu-based streaming-to-DRAM no longer supported (rdar://150685905 (APT: remove legacy multbuf code from xnu)), use --CPUTrace:driver=1"
- "MachOUniversalBinary::ObjectForArch::getAsObjectFile() called when Parent is a nullptr"
- "Multiple shared caches are unsupported (rdar://106054931): tracking "
- "This happened because the device is not provisioned to record a Processor Trace. Try navigating to Settings and enabling Processor Trace."
- "` in your `apple-hwtrace record ...` invocation to fix this. If using `trace record`, see rdar://111873589 for a workaround."
- "libhwtrace @ tag libhwtrace-133.0.2"
- "libhwtrace @ tag libhwtrace-133.0.2\n"

```
