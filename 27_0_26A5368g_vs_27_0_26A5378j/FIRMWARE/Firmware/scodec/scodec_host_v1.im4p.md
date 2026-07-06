## scodec_host_v1.im4p

> `Firmware/scodec/scodec_host_v1.im4p`

```diff

-  __TEXT.__text: 0x4ceac
-  __TEXT.__const: 0x3918
-  __TEXT.__cstring: 0x29a0
+  __TEXT.__text: 0x4ce30
+  __TEXT.__const: 0x3920
+  __TEXT.__cstring: 0x2a23
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x20
   __DATA.__const: 0x7a40

   __DATA.__zerofill: 0x89530
   __OS_LOG.__string: 0x2dab
   Functions: 1068
-  Symbols:   14510
-  CStrings:  731
+  Symbols:   14545
+  CStrings:  734
 
Sections:
~ __DATA.__const : content changed
~ __DATA.__data : content changed
~ __DATA._rtk_patchbay : content changed
~ __DATA._rtk_mtab : content changed
~ __DATA._afk_sys_objt : content changed
~ __DATA.__mod_init_func : content changed
Symbols:
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CE2byo/Sources/RTKit_debug/src/arch/armv8/
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CE2byo/Sources/RTKit_debug/src/arch/armv8/../arm/hibernate/armv8/
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CE2byo/Sources/RTKit_debug/src/arch/armv8/./start_anywhere/
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CE2byo/Sources/RTKit_debug/src/lib/c11/
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CE2byo/Sources/RTKit_debug/src/lib/c11/string//armv8/
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RctSwa/Sources/AppleSCFirmware/./build/scodec_host_v1/scodec_host_v1.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RctSwa/Sources/AppleSCFirmware/source/
+ _OUTLINED_FUNCTION_632
+ _OUTLINED_FUNCTION_633
+ _OUTLINED_FUNCTION_634
+ _OUTLINED_FUNCTION_635
+ _OUTLINED_FUNCTION_636
+ __ZN7RTKHeap11allocCreateEPvmb
+ __ZN7RTKHeap12releaseBlockEPv
+ __cputrace_deadzone_reset
+ iop_ringbuffer_available_size
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LPCBQ0/Sources/RTKit_debug/src/arch/armv8/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LPCBQ0/Sources/RTKit_debug/src/arch/armv8/../arm/hibernate/armv8/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LPCBQ0/Sources/RTKit_debug/src/arch/armv8/./start_anywhere/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LPCBQ0/Sources/RTKit_debug/src/lib/c11/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.LPCBQ0/Sources/RTKit_debug/src/lib/c11/string//armv8/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qMLpt4/Sources/AppleSCFirmware/./build/scodec_host_v1/scodec_host_v1.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qMLpt4/Sources/AppleSCFirmware/source/
- __cputrace_set_stream_base
- _iop_ringbuffer_available_size
CStrings:
+ "start + size <= instance->_region.buffer.size"
+ "start == write_offset"
+ "start > instance->_region.buffer.size - 1024 * cache_line_size"

```
