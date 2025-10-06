## AppleCVHWA

> `/System/Library/PrivateFrameworks/AppleCVHWA.framework/AppleCVHWA`

```diff

-3.2.6.0.0
-  __TEXT.__text: 0x85c38
-  __TEXT.__auth_stubs: 0xba0
-  __TEXT.__const: 0x2a59
-  __TEXT.__gcc_except_tab: 0x3198
-  __TEXT.__cstring: 0x71ec
-  __TEXT.__oslogstring: 0x57f
-  __TEXT.__unwind_info: 0x197c
+3.2.8.0.0
+  __TEXT.__text: 0x8c9b0
+  __TEXT.__auth_stubs: 0xc00
+  __TEXT.__const: 0x2b19
+  __TEXT.__gcc_except_tab: 0x343c
+  __TEXT.__cstring: 0x78a1
+  __TEXT.__oslogstring: 0x13b9
+  __TEXT.__unwind_info: 0x19ec
   __TEXT.__eh_frame: 0xc4
   __TEXT.__objc_methname: 0x25
   __TEXT.__objc_stubs: 0x20
-  __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0x120
+  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__const: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x8
-  __AUTH_CONST.__const: 0xe80
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__auth_got: 0x5e0
+  __AUTH_CONST.__const: 0x50
+  __AUTH_CONST.__auth_got: 0x610
   __DATA.__got_weak: 0x8
   __DATA.__data: 0x92a0
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x5e0
+  __DATA_DIRTY.__const: 0xe50
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 334B8777-161E-3913-BC18-E685E0FBEA41
-  Functions: 1748
-  Symbols:   404
-  CStrings:  485
+  UUID: 9481D55B-7102-3D58-8F90-656AF8B8EE8A
+  Functions: 1877
+  Symbols:   412
+  CStrings:  622
 
Symbols:
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEj
+ __os_log_fault_impl
+ __xpc_error_key_description
+ __xpc_type_error
+ _gettimeofday
+ _localtime
+ _xpc_dictionary_get_string
+ _xpc_get_type
CStrings:
+ "\t\t"
+ "\t\tVRF "
+ " = ("
+ " = 0x"
+ "%F %T"
+ "%{public}s"
+ "(code_address >= (lacc_phys_base_address + itcm_base_addr) && itcm_range_max_ <= itcm_top_addr) && \"Accelerator code extends outside the ITCM range.\""
+ "(data_address >= (lacc_phys_base_address + dtcm_base_addr) && dtcm_range_max_ <= dtcm_top_addr) && \"Accelerator data extends outside the DTCM range.\""
+ "(stack_address >= (dtcm_base_addr) && stack_alloc_end_addr_ <= dtcm_top_addr) && \"Accelerator stack extends outside of DTCM range.\""
+ ")"
+ "********* ******** ******* ****** ***** **** *** ** * Failed to create ISP session in XPCServer: error %u"
+ ", "
+ "---- Accelerator Configuration ----"
+ "---- AppleCVHWA analytics output starts here ----"
+ "---- Client Statistics ----"
+ "0x"
+ "===== HW version %08x ====="
+ "================ Post-execution State ==============="
+ "Bhalt: %d, Bpc: %08x, ICtrStMk0: 0x%08x, ICtrStMk1: 0x%08x, ICtrStMk2: 0x%08x"
+ "CVHWA"
+ "Cached accelerator offload failed due to %{public}s, aborting."
+ "Cancelled the existing XPC/Daemon client connection"
+ "CompleteBuffers failed with error code %d"
+ "DMAMode: %d\t|\tRMA modes: %d, %d, %d, %d\t|\tWMA modes: %d, %d, %d, %d"
+ "ErrClean: %d"
+ "Error addr = 0x%08x_%08x, size = %d, source = %08x"
+ "Error in VisionHWARequestProcessISPSession: error %u, cached=%d"
+ "Expected XPC reply to be a dictionary, but got XPC_TYPE_ERROR"
+ "Failed to create a new XPC/Daemon Client connection"
+ "Failed to create an ISP session with buffers in XPCServer: error code %u"
+ "Failed to create an XPC/Daemon Client connection"
+ "Failed to successfully complete outstanding requests %d"
+ "Final HALT location = %08x"
+ "GRF "
+ "General Processing call failed (HwGPWrapper::RunL...Program)"
+ "HwGPWrapper::LoadProgram Error: Accelerator platform not available"
+ "HwGPWrapper::LoadProgram Error: Binary does not match the platform"
+ "HwGPWrapper::LoadProgram Error: Binary file %s not found."
+ "HwGPWrapper::LoadProgram Error: No daemon connection"
+ "HwGPWrapper::LoadProgram Error: unspecified error #%u"
+ "HwGPWrapper::RunL...Program() -- error code returned by daemon: %d"
+ "ISP driver reported error %d for processing buffer."
+ "ISP driver reported error %d for processing buffer. Max number of retries reached."
+ "ISP temporarily unavailable -- retrying. Driver reported code %d."
+ "LC0 = %08x, LC1 = %08x, LC2 = %08x, LC3 = %08x, RET = %08x"
+ "Load requests sent by client: %d, most recently at %{public}s.%06d"
+ "Lookup requests sent by client: %d, most recently at %{public}s.%06d"
+ "Metadata register values are stale, not reporting."
+ "No stack frame allocated for accelerator -- cannot run without it!"
+ "One or more control buffer pointers are NULL in call to HwGPWrapper::RunLaccProgram"
+ "One or more input buffer pointers are NULL in call to HwGPWrapper::RunLaccProgram"
+ "One or more output buffer pointers are NULL in call to HwGPWrapper::RunLaccProgram"
+ "Original error reported by request utility function: "
+ "PRF %d = %d\t\tVRP %d = %02x"
+ "Processing Session created at %{public}s.%06d"
+ "Processing requests sent by client: %d"
+ "RET = 0x"
+ "RMA%zu base 0x%08x_%08x, size %d"
+ "RMA%zu is set by daemon"
+ "ReadStackArgument called, but offset and/or length are out of range."
+ "ReconnectSession: connection=%p, client_id=%llu"
+ "Releasing and re-allocating a DMA buffer :("
+ "STAT0 = %08x, STAT1 = %08x, STAT2 = %08x, halt status = %d"
+ "Symbol %s was not found"
+ "Uncached accelerator offload failed due to %{public}s, aborting."
+ "VisionHWACancelXPCConnection: Cancelling XPC connection %p"
+ "VisionHWAClient: Creating XPC connection to %s: %p"
+ "VisionHWAClient: Error %s received from daemon"
+ "VisionHWAClient: XPC Connection Cancelled"
+ "WMA%zu start 0x%08x_%08x, size %d"
+ "XPC Connection created at %{public}s.%06d"
+ "XPC reply error: %{public}s"
+ "an unexpected halt address -- possibly an assertion in the accelerator kernel."
+ "call with invalid return address"
+ "d CntBrp: %d, enabled: %d, pipe-clean: %d"
+ "d DtAdBrpBsAd[0..3]: 0x%08x 0x%08x 0x%08x 0x%08x"
+ "d DtAdBrpEOf[0..3]: 0x%08x 0x%08x 0x%08x 0x%08x"
+ "d DtAdBrpEn[0..3]: %d %d %d %d"
+ "d DtAdBrpPCl: %d"
+ "d En: %d"
+ "d PCBrpEn[0..3]: %d %d %d %d"
+ "d PCBrpPCl: %d"
+ "d PCBrp[0..3]: 0x%08x 0x%08x 0x%08x 0x%08x"
+ "d StBrpMk[0..2]: 0x%08x 0x%08x 0x%08x, pipe-clean: %d"
+ "incomplete offload call"
+ "incomplete offload call -- function symbol not found"
+ "incomplete offload call -- return symbol not found"
+ "incomplete offload call -- unable to load program"
+ "incomplete offload call -- unable to reconnect"
+ "isp_ && \"Failed to instantiate an ISP driver plugin\""
+ "kVisionHWAReturnArchMismatch"
+ "kVisionHWAReturnBufferAllocationFailed"
+ "kVisionHWAReturnBufferListSizeInvalid"
+ "kVisionHWAReturnBufferReconstitutionFailed"
+ "kVisionHWAReturnBufferUpdateFailed"
+ "kVisionHWAReturnClientIdMismatch"
+ "kVisionHWAReturnClientIdNotFound"
+ "kVisionHWAReturnCommandInvalid"
+ "kVisionHWAReturnConnectionFailure"
+ "kVisionHWAReturnElfFileNotFound"
+ "kVisionHWAReturnElfPathNotAbsolute"
+ "kVisionHWAReturnError"
+ "kVisionHWAReturnFileSystemError"
+ "kVisionHWAReturnGeneralProcessingFailed"
+ "kVisionHWAReturnInvalidArgument"
+ "kVisionHWAReturnInvalidContext"
+ "kVisionHWAReturnInvalidSession"
+ "kVisionHWAReturnIoSurfaceFailure"
+ "kVisionHWAReturnIspDeviceCreationFailed"
+ "kVisionHWAReturnIspDeviceNotAvailable"
+ "kVisionHWAReturnLoadProgramFailed"
+ "kVisionHWAReturnMalformedReply"
+ "kVisionHWAReturnNoError"
+ "kVisionHWAReturnNonSystemVolumeFilePath"
+ "kVisionHWAReturnOutOfMemory"
+ "kVisionHWAReturnPathArgumentMissing"
+ "kVisionHWAReturnPixelBufferNotCreated"
+ "kVisionHWAReturnPlatformUnavailable"
+ "kVisionHWAReturnSessionCreationFailed"
+ "kVisionHWAReturnSessionNotAvailable"
+ "kVisionHWAReturnSessionPreparationFailed"
+ "kVisionHWAReturnSetCompletionCallbackFailed"
+ "kVisionHWAReturnSymbolArgumentMissing"
+ "kVisionHWAReturnSymbolNotFound"
+ "kVisionHWAReturnSymbolSizeNotAvailable"
+ "kVisionHWAReturnUnknownFailure"
+ "prof BP HCnt: %d"
+ "prof BP MCnt: %d"
+ "prof Clr: %d"
+ "prof Dt BCont StCnt: %d"
+ "prof Dt LCont StCnt: %d"
+ "prof Dt SCont StCnt: %d"
+ "prof En: %d"
+ "prof FR Cnt: %d"
+ "prof H Cnt: %d"
+ "prof Hz StCnt: %d"
+ "prof It BCont StCnt: %d"
+ "prof Mbr StCnt: %d"
+ "prof Pk Cnt: %d"
+ "prof Pp ClStCnt: %d"
+ "prof SB Dr StCnt: %d"
+ "prof bus StCnt: %d"
+ "unexpected program counter: 0x%08x."
- "%s"
- "(code_address >= (lacc_phys_base_address + itcm_base_addr) && itcm_range_max_ <= itcm_top_addr) && \"Start of LACC code is outside of ITCM range.\""
- "(data_address >= (lacc_phys_base_address + dtcm_base_addr) && dtcm_range_max_ <= dtcm_top_addr) && \"Start of LACC data is outside of DTCM range.\""
- "(stack_address >= (dtcm_base_addr) && stack_alloc_end_addr_ <= dtcm_top_addr) && \"LACC stack extends outside of DTCM range.\""
- "Error: Failed to successfully complete outstanding requests %d"
- "isp_ && \"ISP instance has to be available\""
- "unexpected LACC PC value."

```
