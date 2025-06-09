## AppleCVHWA

> `/System/Library/PrivateFrameworks/AppleCVHWA.framework/AppleCVHWA`

```diff

-3.7.1.0.0
-  __TEXT.__text: 0xad030
-  __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__const: 0x2b79
-  __TEXT.__gcc_except_tab: 0x5588
-  __TEXT.__cstring: 0x7f59
-  __TEXT.__oslogstring: 0x1646
-  __TEXT.__unwind_info: 0x14d0
+4.2.1.0.0
+  __TEXT.__text: 0xad00c
+  __TEXT.__auth_stubs: 0xc60
+  __TEXT.__const: 0x2e08
+  __TEXT.__gcc_except_tab: 0x57bc
+  __TEXT.__oslogstring: 0x317
+  __TEXT.__cstring: 0x8025
+  __TEXT.__unwind_info: 0x1640
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_methname: 0x25
   __TEXT.__objc_stubs: 0x20
   __DATA_CONST.__got: 0x1f8
-  __DATA_CONST.__const: 0x238
+  __DATA_CONST.__const: 0x288
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x5f8
-  __AUTH_CONST.__const: 0x10c0
-  __AUTH_CONST.__cfstring: 0x60
+  __AUTH_CONST.__auth_got: 0x640
+  __AUTH_CONST.__const: 0x1368
+  __AUTH_CONST.__cfstring: 0x240
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__data: 0x20
-  __DATA.__data: 0x94ec
-  __DATA.__crash_info: 0x40
+  __DATA.__data: 0x952c
+  __DATA.__crash_info: 0x148
   __DATA.__llvm_prf_cnts: 0x98
   __DATA.__llvm_prf_data: 0x80
   __DATA.__llvm_prf_names: 0x12b8
-  __DATA.__bss: 0x560
-  __DATA.__common: 0x20
+  __DATA.__bss: 0x578
+  __DATA.__common: 0x30
   __LLVM_COV.__llvm_covfun: 0xd6d6
   __LLVM_COV.__llvm_covmap: 0x164
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2A582892-1ED1-3C1E-93DD-E7E0DBC9D793
-  Functions: 992
-  Symbols:   437
-  CStrings:  679
+  UUID: B8FCA95E-3F35-3E8B-B7B3-9117D0D333B9
+  Functions: 1055
+  Symbols:   447
+  CStrings:  599
 
Symbols:
+ _MGCopyAnswer
+ _MGGetSInt32Answer
+ _MGGetSInt64Answer
+ _MGGetStringAnswer
+ __ZNSt3__113basic_filebufIcNS_11char_traitsIcEEE5closeEv
+ __ZNSt3__113basic_filebufIcNS_11char_traitsIcEEEC1Ev
+ __ZNSt3__113basic_filebufIcNS_11char_traitsIcEEED1Ev
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEE4readEPcl
+ __ZNSt3__113basic_istreamIcNS_11char_traitsIcEEED2Ev
+ __ZNSt3__114basic_ifstreamIcNS_11char_traitsIcEEE4openEPKcj
+ __ZNSt3__14__fs10filesystem11__file_sizeERKNS1_4pathEPNS_10error_codeE
+ __ZNSt3__16localeC1Ev
+ __ZTISt9exception
+ __ZTTNSt3__114basic_ifstreamIcNS_11char_traitsIcEEEE
+ __ZTVNSt3__114basic_ifstreamIcNS_11char_traitsIcEEEE
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ ___cxa_pure_virtual
+ _os_retain
+ _stat
- _MGGetProductType
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __Znwm
- __xpc_error_connection_interrupted
- __xpc_error_connection_invalid
- __xpc_error_key_description
- __xpc_error_termination_imminent
- _xpc_dictionary_get_string
CStrings:
+ "%p %c: %m%n"
+ "+N9mZUAHooNvMiQnjeTJ8g"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/include/VIO/HWFeatureDetection/HwProcessOutputUtilsImpl.h"
+ "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwTahiti.cpp"
+ "/System/Library/PrivateFrameworks/AppleCVHWA.framework/Firmware/"
+ "BuildVersion"
+ "Call to LACC with invalid return address set (RET register)"
+ "CameraIMUDistanceType"
+ "ChipID"
+ "ComputerName"
+ "GraphicsFeatureSetClass"
+ "GraphicsFeatureSetFallbacks"
+ "H15"
+ "H16"
+ "H17"
+ "HWModelStr"
+ "InternalBuild"
+ "IsVirtualDevice"
+ "ProductVersion"
+ "RearFacingCameraTimeOfFlightCameraCapability"
+ "ReleaseType"
+ "SerialNumber"
+ "cannot find tid kernel"
+ "com.apple.AppleCVHWA"
+ "cvhwa"
+ "cvhwa.gpapi"
+ "cvhwa.vio"
+ "data_segment_size <= kDataSegmentSize && \"Data segment size larger than expected\""
+ "invalid bin size"
+ "lacc_DpKernel.bin"
+ "lacc_buffer_size >= input_size"
+ "marketing-name"
+ "rb"
+ "unsupported platform"
- "%s %s, error %d"
- "%s %s: file does not exist."
- "%{public}s"
- "********* ******** ******* ****** ***** **** *** ** * Failed to create ISP session in XPCServer: error %u"
- "---- Accelerator Configuration ----"
- "---- AppleCVHWA analytics output starts here ----"
- "---- Client Statistics ----"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/include/VIO/HWFeatureDetection/HwLaccUtilsImpl.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwCollUtils.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCVHWA/library/VIO/HWFeatureDetection/src/HwTahiti-D93.cpp"
- "===== HW version %08x ====="
- "================ Post-execution State ==============="
- "Bhalt: %d, Bpc: %08x, ICtrStMk0: 0x%08x, ICtrStMk1: 0x%08x, ICtrStMk2: 0x%08x"
- "Cached accelerator offload failed due to %{public}s, aborting."
- "Could not load accelerator binary."
- "Could not reconnect to XPC service"
- "DMAMode: %d\t|\tRMA modes: %d, %d, %d, %d\t|\tWMA modes: %d, %d, %d, %d"
- "ErrClean: %d"
- "Error addr = 0x%08x_%08x, size = %d, source = %08x"
- "Error in VisionHWARequestProcessISPSession: error %u, cached=%d"
- "Failed to create XPC object from IOSurface"
- "Failed to create an XPC/Daemon Client connection"
- "Failed to execute symbol lookup on daemon -- daemon may have restarted. Trying to reconnect."
- "Failed to load program -- Aborting."
- "Failed to obtain IOSurface from CVPixelBuffer"
- "Final HALT location = %08x"
- "General Processing call failed (HwGPWrapper::RunL...Program)"
- "HasHardwareFeaturePointsTahiti() && \"Configuration not supported.\""
- "HwGPWrapper::LoadProgram Error: Accelerator platform not available"
- "HwGPWrapper::LoadProgram Error: Binary does not match the platform"
- "HwGPWrapper::LoadProgram Error: Binary file %s not found."
- "HwGPWrapper::LoadProgram Error: No daemon connection"
- "HwGPWrapper::LoadProgram Error: unspecified error #%u"
- "HwGPWrapper::RunL...Program() -- error code returned by daemon: %d"
- "LC0 = %08x, LC1 = %08x, LC2 = %08x, LC3 = %08x, RET = %08x"
- "Lacc config and metadata received\n"
- "Load requests sent by client: %d, most recently at %{public}s.%06d"
- "Lookup requests sent by client: %d, most recently at %{public}s.%06d"
- "Lost connection to daemon"
- "Metadata register values are stale, not reporting."
- "No stack frame allocated for accelerator -- cannot run without it!"
- "Offload call failed with transient error -- number of retries left: %d."
- "One or more control buffer pointers are NULL in call to HwGPWrapper::RunLaccProgram"
- "One or more input buffer pointers are NULL in call to HwGPWrapper::RunLaccProgram"
- "One or more output buffer pointers are NULL in call to HwGPWrapper::RunLaccProgram"
- "Out.rslt"
- "PRF %d = %d\t\tVRP %d = %02x"
- "Processing Session created at %{public}s.%06d"
- "Processing requests sent by client: %d"
- "RMA%zu base 0x%08x_%08x, size %d"
- "RMA%zu is set by daemon"
- "ReadStackArgument called, but offset and/or length are out of range."
- "ReconnectSession: Failed to create a new XPC connection"
- "ReconnectSession: Failed to create an ISP session with buffers -- error code %u"
- "ReconnectSession: connection=%p, client_id=%llu"
- "Releasing and re-allocating a DMA buffer :("
- "ReplyChecker XPC error: %s"
- "ReplyChecker error: XPC connection interrupted"
- "ReplyChecker error: XPC connection invalid"
- "ReplyChecker error: XPC connection termination imminent"
- "STAT0 = %08x, STAT1 = %08x, STAT2 = %08x, halt status = %d"
- "Symbol %s was not found"
- "Symbol lookup on daemon failed repeatedly -- Aborting."
- "TID %u, %s duplicate"
- "Uncached accelerator offload failed due to %{public}s, aborting."
- "Use of XPC Services %d"
- "VisionHWACancelXPCConnection: Cancelling XPC connection %p"
- "VisionHWAClient error: malformed reply from daemon"
- "VisionHWAClient: Creating XPC connection to %s: %p"
- "VisionHWAClient: Error %s received from daemon"
- "VisionHWAClient: Invalid Buffer list size %d"
- "VisionHWAClient: Invalid Input xpc object!!\n"
- "VisionHWAClient: Invalid actionXPCSurface!!\n"
- "VisionHWAClient: Invalid cmdBufSurfaceAction!!\n"
- "VisionHWAClient: Invalid cmdBufSurfaceIO!!\n"
- "VisionHWAClient: Invalid cmdBufSurfaceOperation!!\n"
- "VisionHWAClient: Invalid cmdBufSurfaceStats!!\n"
- "VisionHWAClient: Invalid ioXPCSurface!!\n"
- "VisionHWAClient: Invalid operationXPCSurface!!\n"
- "VisionHWAClient: Invalid process buffer info\n"
- "VisionHWAClient: Invalid statsXPCSurface!!\n"
- "VisionHWAClient: Invalid xpc connection!!\n"
- "VisionHWAClient: XPC Connection Cancelled"
- "VisionHWAServer: Unable to open ELF binary"
- "WMA%zu start 0x%08x_%08x, size %d"
- "XPC Connection created at %{public}s.%06d"
- "[AppleCVHWA] curr to same prev: %u & %u -> %u."
- "[AppleCVHWA] skipped %u matches potentially due to frame drop - matches correspond to new untracked features in dropped frame"
- "base_addr != nullptr && \"address cannot be null\""
- "call with invalid return address"
- "com.apple.cv3d"
- "curr & prev idx"
- "curr index: %u is duplicate"
- "curr to prev: %u -> %u."
- "cv3d.vio"
- "d CntBrp: %d, enabled: %d, pipe-clean: %d"
- "d DtAdBrpEOf[0..3]: 0x%08x 0x%08x 0x%08x 0x%08x"
- "d DtAdBrpEn[0..3]: %d %d %d %d"
- "d DtAdBrpPCl: %d"
- "d En: %d"
- "d PCBrpEn[0..3]: %d %d %d %d"
- "d PCBrpPCl: %d"
- "d PCBrp[0..3]: 0x%08x 0x%08x 0x%08x 0x%08x"
- "d StBrpMk[0..2]: 0x%08x 0x%08x 0x%08x, pipe-clean: %d"
- "duplicate indices pair: {%u, %u}"
- "height = %d"
- "lacc_buffer_size >= input_size && \"buffer size cannot be more than input\""
- "lacc_buffer_size >= lacc_tahiti_dp_bin_len"
- "prev index: %u is duplicate"
- "prof BP HCnt: %d"
- "prof BP MCnt: %d"
- "prof Clr: %d"
- "prof Dt BCont StCnt: %d"
- "prof Dt LCont StCnt: %d"
- "prof Dt SCont StCnt: %d"
- "prof En: %d"
- "prof FR Cnt: %d"
- "prof H Cnt: %d"
- "prof Hz StCnt: %d"
- "prof It BCont StCnt: %d"
- "prof Mbr StCnt: %d"
- "prof Pk Cnt: %d"
- "prof Pp ClStCnt: %d"
- "prof SB Dr StCnt: %d"
- "prof bus StCnt: %d"
- "stride = %d"
- "unexpected program counter: 0x%08x."
- "width = %d"

```
