## ScreensharingAgent

> `/System/Library/CoreServices/RemoteManagement/ScreensharingAgent.bundle/Contents/MacOS/ScreensharingAgent`

```diff

-  __TEXT.__text: 0x48b44
-  __TEXT.__auth_stubs: 0x1ba0
+  __TEXT.__text: 0x489b8
+  __TEXT.__auth_stubs: 0x1b90
   __TEXT.__objc_stubs: 0x2ac0
   __TEXT.__objc_methlist: 0xea8
   __TEXT.__const: 0x6ca
-  __TEXT.__oslogstring: 0x86d3
-  __TEXT.__cstring: 0x15974
+  __TEXT.__oslogstring: 0x8995
+  __TEXT.__cstring: 0x15d4d
   __TEXT.__gcc_except_tab: 0xb4
   __TEXT.__objc_methname: 0x2fe5
   __TEXT.__objc_classname: 0x1a1
   __TEXT.__objc_methtype: 0xa3c
-  __TEXT.__unwind_info: 0x6e0
-  __DATA_CONST.__const: 0x10a8
-  __DATA_CONST.__cfstring: 0x900
+  __TEXT.__unwind_info: 0x6e8
+  __DATA_CONST.__const: 0x1278
+  __DATA_CONST.__cfstring: 0x880
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0xde0
-  __DATA_CONST.__got: 0x398
+  __DATA_CONST.__auth_got: 0xdd8
+  __DATA_CONST.__got: 0x3b0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x14c0
   __DATA.__objc_selrefs: 0xda0
   __DATA.__objc_ivar: 0xd0
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x3328
-  __DATA.__bss: 0x328c
+  __DATA.__bss: 0x3274
   __DATA.__common: 0x263d
   __CGPreLoginApp.__cgpreloginapp: 0x0
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio

   - /System/Library/Frameworks/OpenCL.framework/Versions/A/OpenCL
   - /System/Library/Frameworks/OpenGL.framework/Versions/A/OpenGL
   - /System/Library/Frameworks/ScreenCaptureKit.framework/Versions/A/ScreenCaptureKit
+  - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/VideoToolbox.framework/Versions/A/VideoToolbox
   - /System/Library/PrivateFrameworks/AVConference.framework/Versions/A/AVConference
   - /System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/Versions/A/AccessibilitySharedSupport

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 824
-  Symbols:   567
-  CStrings:  3405
+  Functions: 881
+  Symbols:   566
+  CStrings:  3417
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA.__common : content changed
Symbols:
+ _CFBooleanGetValue
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateWithAuditToken
- _dlclose
- _dlopen
- _dlsym
- _stat
CStrings:
+ "\"%s\""
+ "(empty)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/LockScreen/LockScreenCommon.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/RFBCommon/CheckScreenSharingEntitlement.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/RFBCommon/Clipboard.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/RFBCommon/HEVCFrameRate.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/RFBCommon/KeyMap.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/RFBCommon/MouseEventUtils.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/RFBCommon/RFBCommon.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/RFBServer/AutoPasteboardTimer.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/RFBServer/DisplayNotification.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/RFBServer/EncodeMultiVariant.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/RFBServer/EncodeMultiVariantCL.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/RFBServer/HuffmanEncode.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/RFBServer/OpenGLUtils.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/RFBServer/RFBServerUtils.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/RFBServer/SSAgentScreenCapture.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/RFBServer/ScreenWake.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/RFBServer/SendFrameBufferOpenCL.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/RFBServer/hidpi.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/SSAssistanceCursor/SSAssistanceCursorIPC.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/SSPasteboardHelper/SSPasteboardHelperIPC.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/ScreensharingAgent/AgentGuestAccessIPC.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/ScreensharingAgent/AgentScrapIPC.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/ScreensharingAgent/AgentScreenState.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/ScreensharingAgent/AgentViewer.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/ScreensharingAgent/SSAgentVirtualDisplay.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/ScreensharingAgent/SSUDPSender.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/ScreensharingAgent/ScreensharingAgent.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/ScreensharingAgent/WindowserverCommunication.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/common/CommonUtilities.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/common/Log.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/common/MenuExtraHelper.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/common/OSVersionUtils.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/common/RDSemaphore.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/common/RDSemaphore.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/common/RDThread.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/common/SSSignposts.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XY1mEG/Sources/RemoteDesktop/common/SSTimebase.m"
+ "Agent_EncodeMVSCL"
+ "Agent_EncodeMVSCL failed (%d) - dropping frame"
+ "CL error %s (%d) at %s:%d"
+ "CL error (%d) creating command_mem at %s:%d"
+ "CL error (%d) creating render_mem at %s:%d"
+ "CL error (%d) mapping command buffer"
+ "CL error (%d) mapping render buffer at %s:%d"
+ "CL_BUILD_PROGRAM_FAILURE"
+ "CL_EXEC_STATUS_ERROR_FOR_EVENTS_IN_WAIT_LIST"
+ "CL_IMAGE_FORMAT_NOT_SUPPORTED"
+ "CL_INVALID_ARG_INDEX"
+ "CL_INVALID_ARG_SIZE"
+ "CL_INVALID_ARG_VALUE"
+ "CL_INVALID_COMMAND_QUEUE"
+ "CL_INVALID_CONTEXT"
+ "CL_INVALID_EVENT_WAIT_LIST"
+ "CL_INVALID_GLOBAL_OFFSET"
+ "CL_INVALID_IMAGE_SIZE"
+ "CL_INVALID_KERNEL"
+ "CL_INVALID_KERNEL_ARGS"
+ "CL_INVALID_MEM_OBJECT"
+ "CL_INVALID_PROGRAM"
+ "CL_INVALID_PROGRAM_EXECUTABLE"
+ "CL_INVALID_SAMPLER"
+ "CL_INVALID_VALUE"
+ "CL_INVALID_WORK_DIMENSION"
+ "CL_INVALID_WORK_GROUP_SIZE"
+ "CL_INVALID_WORK_ITEM_SIZE"
+ "CL_MAP_FAILURE"
+ "CL_MEM_OBJECT_ALLOCATION_FAILURE"
+ "CL_MISALIGNED_SUB_BUFFER_OFFSET"
+ "CL_OUT_OF_HOST_MEMORY"
+ "CL_OUT_OF_RESOURCES"
+ "CL_SUCCESS"
+ "CheckScreenSharingEntitlement"
+ "Error on CaptureAndResizeScreen %d"
+ "Failed to build program, err=%d"
+ "Failed to create DCT quantization table, err=%d"
+ "Failed to create kernel, err=%d"
+ "Failed to create program from source, err=%d"
+ "Failed to get program build error log size, err=%d"
+ "Failed to read program build log contents, err=%d"
+ "Program build error log:"
+ "SecTaskCopyValueForEntitlement failed: %s"
+ "StitchBuffers"
+ "StitchBuffers failed (%d) in Agent_EncodeMVSCL"
+ "Unable to create task for audit token"
+ "clCreateImage2D for dstImg failed (err=%d, dstW=%zu, dstH=%zu)"
+ "clCreateImage2D for resampling filter failed (err=%d, kWidth=%d, samResolution=%d, scale=%f)"
+ "clCreateImage2D for tmpImg failed (err=%d, tmpW=%zu, tmpH=%zu)"
+ "clCreateImageFromIOSurface2DAPPLE failed (%d) at %s:%d (w=%d h=%d)"
+ "clCreateResamplingFilter"
+ "clEnqueueNDRangeKernel(kerX) failed (%d) - skipping kerY enqueue"
+ "clEnqueueNDRangeKernel(kerY) failed (%d)"
+ "clEnqueueUnmapMemObject(command_mem) failed (%d)"
+ "clEnqueueUnmapMemObject(command_mem) failed (%d) during render-map bail"
+ "clEnqueueUnmapMemObject(command_mem) failed (%d) during wait-error bail"
+ "clEnqueueUnmapMemObject(render_mem) failed (%d)"
+ "clEnqueueUnmapMemObject(render_mem) failed (%d) during wait-error bail"
+ "clSetKernelArg for kerX failed (accumulated err=%d)"
+ "clSetKernelArg for kerY failed (accumulated err=%d)"
+ "clSetKernelArg(0) failed (%d) in clEncodingInfo_Initialize"
+ "clSetKernelArg(1) failed (%d) in clEncodingInfo_Initialize"
+ "clWaitForEvents failed (%d) in StitchBuffers - skipping frame"
+ "com.apple.private.screensharing.xpcaccepted"
+ "has entitlement = %d"
+ "log: %s "
+ "malloc failed for build log (size %zu)"
+ "malloc failed for build log (size %zu) in clCreateResizingPlan"
+ "malloc failed for resampling filter buffers (kWidth=%d, nSamples=%d)"
+ "unrecognized CL error"
- "\n\n %s \n\n"
- "\"%s\"\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/LockScreen/LockScreenCommon.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/RFBCommon/Clipboard.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/RFBCommon/HEVCFrameRate.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/RFBCommon/KeyMap.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/RFBCommon/MouseEventUtils.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/RFBCommon/RFBCommon.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/RFBServer/AutoPasteboardTimer.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/RFBServer/DisplayNotification.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/RFBServer/EncodeMultiVariant.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/RFBServer/EncodeMultiVariantCL.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/RFBServer/HuffmanEncode.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/RFBServer/OpenGLUtils.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/RFBServer/RFBServerUtils.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/RFBServer/SSAgentScreenCapture.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/RFBServer/ScreenWake.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/RFBServer/SendFrameBufferOpenCL.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/RFBServer/hidpi.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/SSAssistanceCursor/SSAssistanceCursorIPC.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/SSPasteboardHelper/SSPasteboardHelperIPC.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/ScreensharingAgent/AgentGuestAccessIPC.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/ScreensharingAgent/AgentScrapIPC.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/ScreensharingAgent/AgentScreenState.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/ScreensharingAgent/AgentViewer.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/ScreensharingAgent/SSAgentVirtualDisplay.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/ScreensharingAgent/SSUDPSender.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/ScreensharingAgent/ScreensharingAgent.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/ScreensharingAgent/WindowserverCommunication.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/common/CommonUtilities.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/common/Log.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/common/MenuExtraHelper.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/common/OSVersionUtils.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/common/RDSemaphore.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/common/RDSemaphore.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/common/RDThread.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/common/SSSignposts.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6BSGD4/Sources/RemoteDesktop/common/SSTimebase.m"
- "/System/Library/Frameworks/Security.framework/Security"
- "/var/db/.RemoteManagementDebugAdmin"
- "AssertNoError"
- "CL error (%d) at %s:%d\t"
- "CL_EXEC_STATUS_ERROR_FOR_EVENTS_IN_WAIT_LIST\n"
- "CL_INVALID_ARG_INDEX\n"
- "CL_INVALID_ARG_SIZE\n"
- "CL_INVALID_ARG_VALUE\n"
- "CL_INVALID_COMMAND_QUEUE\n"
- "CL_INVALID_CONTEXT\n"
- "CL_INVALID_EVENT_WAIT_LIST\n"
- "CL_INVALID_GLOBAL_OFFSET\n"
- "CL_INVALID_KERNEL\n"
- "CL_INVALID_KERNEL_ARGS\n"
- "CL_INVALID_MEM_OBJECT\n"
- "CL_INVALID_PROGRAM_EXECUTABLE\n"
- "CL_INVALID_SAMPLER\n"
- "CL_INVALID_VALUE\n"
- "CL_INVALID_WORK_DIMENSION\n"
- "CL_INVALID_WORK_GROUP_SIZE\n"
- "CL_INVALID_WORK_ITEM_SIZE\n"
- "CL_MEM_OBJECT_ALLOCATION_FAILURE\n"
- "CL_MISALIGNED_SUB_BUFFER_OFFSET\n"
- "CL_OUT_OF_HOST_MEMORY\n"
- "CL_OUT_OF_RESOURCES\n"
- "Failed to build program, err=%d\n"
- "Failed to create DCT quantization table, err=%d\n"
- "Failed to create kernel, err=%d\n"
- "Failed to get program build error log, err=%d\n"
- "IsCodeSignatureValid"
- "PrintError"
- "Program build error log:\n"
- "SecCodeCheckValidity"
- "SecCodeCopyGuestWithAttributes"
- "SecCodeCopyGuestWithAttributes error %d"
- "SecRequirementCreateWithString"
- "SecRequirementCreateWithString error %d"
- "anchor apple"
- "anchor apple generic and certificate leaf[field.1.2.840.113635.100.6.1.7] exists and certificate leaf[subject.CN] = \"3rd Party Mac Developer Application: Apple Inc.\"* and certificate 1[field.1.2.840.113635.100.6.2.1] exists"
- "anchor apple generic and info [CFBundleIdentifier] = \"com.apple.\"* and certificate leaf[field.1.2.840.113635.100.6.1.9.1] exists"
- "anchor apple generic and info [CFBundleIdentifier] = \"com.apple.\"* and certificate leaf[field.1.2.840.113635.100.6.1.9] exists"
- "app qa error %d"
- "app store check errror %d"
- "app store test build error %d"
- "apple check errror %d"
- "create requirements for app production build error %d"
- "create requirements for app qa build error %d"
- "create requirements for app store test build error %d"
- "dlopen failed trying to open lib."
- "dlsym failed %p %p %p"
- "pid"
- "return %d"
- "start of check"

```
