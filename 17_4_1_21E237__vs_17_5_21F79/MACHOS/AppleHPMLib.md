## AppleHPMLib

> `/System/Library/Extensions/AppleHPM.kext/PlugIns/AppleHPMLib.plugin/AppleHPMLib`

```diff

-540.100.5.0.0
-  __TEXT.__text: 0x2548
-  __TEXT.__auth_stubs: 0x1b0
-  __TEXT.__oslogstring: 0x491
-  __TEXT.__cstring: 0x1cd
+540.120.2.0.0
+  __TEXT.__text: 0x32d4
+  __TEXT.__auth_stubs: 0x200
+  __TEXT.__cstring: 0x775
+  __TEXT.__oslogstring: 0x55e
   __TEXT.__const: 0x63
   __TEXT.__gcc_except_tab: 0x48
-  __TEXT.__unwind_info: 0x10c
+  __TEXT.__unwind_info: 0x114
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0xe0
-  __DATA_CONST.__got: 0x28
+  __DATA_CONST.__auth_got: 0x108
+  __DATA_CONST.__got: 0x30
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x120
+  __DATA_CONST.__cfstring: 0x20
   __DATA.__data: 0xc8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 52
-  Symbols:   82
-  CStrings:  29
+  Functions: 60
+  Symbols:   90
+  CStrings:  53
 
Symbols:
+ _CFDataGetBytes
+ _CFDataGetLength
+ _IORegistryEntryCreateCFProperty
+ _IORegistryEntryGetParentEntry
+ __ZN15AppleHPMLibPriv6getRIDEv
+ __ZN22AppleHPMLibRTInterfaceC2EPPvyj
+ ___CFConstantStringClassReference
+ _kCFAllocatorDefault
+ _os_parse_boot_arg_string
+ _printf
- __ZN22AppleHPMLibRTInterfaceC2EPPvy
- __os_log_debug_impl
CStrings:
+ "-restore"
+ "AppleHPMLibRT13Interface::%s@0x%llx RID%u - Forcing CIO + USB2 failed\n\n"
+ "AppleHPMLibRT13Interface::%s@0x%llx RID%u - HPM in ADFU\n\n"
+ "AppleHPMLibRT13Interface::%s@0x%llx RID%u - HPM is NOT in ADFU, modeData=0x%x\n\n"
+ "AppleHPMLibRT13Interface::%s@0x%llx RID%u - Not in DFUf but still failed VOUT, modeData=0x%x\n\n"
+ "AppleHPMLibRT13Interface::%s@0x%llx RID%u - Read mode failed [0x%X]\n\n"
+ "AppleHPMLibRT13Interface::%s@0x%llx RID%u - cancelling DFUf failed [0x%X], taskRetCode=0x%X, modeData=0x%x\n\n"
+ "AppleHPMLibRT13Interface::%s@0x%llx RID%u - check for in ADFU failed [0x%X]\n\n"
+ "AppleHPMLibRT13Interface::%s@0x%llx RID%u - entry\n\n"
+ "AppleHPMLibRT13Interface::%s@0x%llx RID%u - entry. enable = 0x%X\n\n"
+ "AppleHPMLibRT13Interface::%s@0x%llx RID%u - entry. value = 0x%X\n\n"
+ "AppleHPMLibRT13Interface::%s@0x%llx RID%u - exit status=0x%X\n\n"
+ "AppleHPMLibRT13Interface::%s@0x%llx RID%u - first VOUT failed, check if HPM is in DFUf [0x%X], taskRetCode=0x%X\n\n"
+ "AppleHPMLibRT13Interface::%s@0x%llx RID%u - pulling HPM out of DFUf...\n\n"
+ "AppleHPMLibRT13Interface::%s@0x%llx RID%u - second VOUT failed, status = [0x%X], taskRetCode=0x%X, modeData=0x%x\n\n"
+ "AppleHPMLibRT13Interface::%s@0x%llx RID%u - trying VOUT after cancelling DFUf, value = 0x%X\n\n"
+ "AppleHPMLibRTInterface"
+ "AppleHPMLibRTInterface::%s@0x%llx RID%u - AppleHPMLibRTUpdater - panic debug enabled:%u\n\n"
+ "AppleHPMLibRTInterface::%s@0x%llx RID%u - Failed to trigger system panic: %u\n"
+ "IOService"
+ "hpmrtlog"
+ "rid"
+ "triggerSystemPanic"
- "AppleHPMLibRTUpdater - panic debug enabled:%u\n"
- "AppleHPMLibRTUpdaterType13::%s@0x%llx - Forcing CIO + USB2 failed\n\n"
- "AppleHPMLibRTUpdaterType13::%s@0x%llx - HPM in ADFU\n\n"
- "AppleHPMLibRTUpdaterType13::%s@0x%llx - HPM is NOT in ADFU, modeData=0x%x\n\n"
- "AppleHPMLibRTUpdaterType13::%s@0x%llx - Not in DFUf but still failed VOUT, modeData=0x%x\n\n"
- "AppleHPMLibRTUpdaterType13::%s@0x%llx - Read mode failed [0x%X]\n\n"
- "AppleHPMLibRTUpdaterType13::%s@0x%llx - cancelling DFUf failed [0x%X], taskRetCode=0x%X, modeData=0x%x\n\n"
- "AppleHPMLibRTUpdaterType13::%s@0x%llx - check for in ADFU failed [0x%X]\n\n"
- "AppleHPMLibRTUpdaterType13::%s@0x%llx - entry\n\n"
- "AppleHPMLibRTUpdaterType13::%s@0x%llx - entry. enable = 0x%X\n\n"
- "AppleHPMLibRTUpdaterType13::%s@0x%llx - entry. value = 0x%X\n\n"
- "AppleHPMLibRTUpdaterType13::%s@0x%llx - first VOUT failed, check if HPM is in DFUf [0x%X], taskRetCode=0x%X\n\n"
- "AppleHPMLibRTUpdaterType13::%s@0x%llx - pulling HPM out of DFUf...\n\n"
- "AppleHPMLibRTUpdaterType13::%s@0x%llx - second VOUT failed, status = [0x%X], taskRetCode=0x%X, modeData=0x%x\n\n"
- "AppleHPMLibRTUpdaterType13::%s@0x%llx - trying VOUT after cancelling DFUf, value = 0x%X\n\n"
- "Failed to trigger system panic: %u"

```
