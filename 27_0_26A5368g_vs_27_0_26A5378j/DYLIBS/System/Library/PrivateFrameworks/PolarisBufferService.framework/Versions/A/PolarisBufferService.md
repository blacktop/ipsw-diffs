## PolarisBufferService

> `/System/Library/PrivateFrameworks/PolarisBufferService.framework/Versions/A/PolarisBufferService`

```diff

-  __TEXT.__text: 0x5ed5c
+  __TEXT.__text: 0x5efb8
   __TEXT.__const: 0x17ec
   __TEXT.__gcc_except_tab: 0x300c
   __TEXT.__cstring: 0x7df1
-  __TEXT.__oslogstring: 0xaf54
+  __TEXT.__oslogstring: 0xb0b4
   __TEXT.__unwind_info: 0x1e70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
   __DATA.__data: 0x3acc
-  __DATA.__bss: 0x180
+  __DATA.__bss: 0x1b0
   __DATA_DIRTY.__common: 0x30d8
-  __DATA_DIRTY.__bss: 0xf0
+  __DATA_DIRTY.__bss: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreVideo.framework/Versions/A/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/librealtime_safety.dylib
   Functions: 2061
   Symbols:   3448
-  CStrings:  1620
+  CStrings:  1625
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH.__data : content changed
~ __AUTH.__thread_vars : content changed
~ __DATA.__data : content changed
Symbols:
+ _ZN17PSResourceFactory18handle_client_diedEP25resfact_client_died_msg_tPK16ps_caller_info_t
+ __Z24handle_allocate_resourceP19resfact_alloc_msg_tjP17PSResourceFactoryPK16ps_caller_info_t
+ __ZN17PSResourceFactory18handle_client_diedEP25resfact_client_died_msg_tPK16ps_caller_info_t
+ __ZN17PSResourceFactory22handle_ringbuffer_infoEP29resfact_ringbuffer_info_msg_tjPK16ps_caller_info_t
+ __ZN17PSResourceFactory25handle_frame_history_infoEP32resfact_frame_history_info_msg_tjPK16ps_caller_info_t
+ __ZN17PSResourceFactory28handleResourceFactoryMessageEP17res_factory_msg_tjP21mach_msg_descriptor_tPK16ps_caller_info_t
+ __ZN17PSResourceFactory28validate_client_entitlementsEP25resfact_register_sb_msg_tjPK16ps_caller_info_t
+ __ZN17PSResourceFactory29handle_register_shbuffergroupEP25resfact_register_sb_msg_tjPK16ps_caller_info_t
+ __ZN17PSResourceFactory31handle_unregister_shbuffergroupEP25resfact_register_sb_msg_tjPK16ps_caller_info_t
+ ____ZN17PSResourceFactory28handleResourceFactoryMessageEP17res_factory_msg_tjP21mach_msg_descriptor_tPK16ps_caller_info_t_block_invoke
- _ZN17PSResourceFactory18handle_client_diedEP25resfact_client_died_msg_t
- __Z24handle_allocate_resourceP19resfact_alloc_msg_tjP17PSResourceFactory
- __ZN17PSResourceFactory18handle_client_diedEP25resfact_client_died_msg_t
- __ZN17PSResourceFactory22handle_ringbuffer_infoEP29resfact_ringbuffer_info_msg_tj
- __ZN17PSResourceFactory25handle_frame_history_infoEP32resfact_frame_history_info_msg_tj
- __ZN17PSResourceFactory28handleResourceFactoryMessageEP17res_factory_msg_tjP21mach_msg_descriptor_ti
- __ZN17PSResourceFactory28validate_client_entitlementsEP25resfact_register_sb_msg_tj13audit_token_t
- __ZN17PSResourceFactory29handle_register_shbuffergroupEP25resfact_register_sb_msg_tj13audit_token_t
- __ZN17PSResourceFactory31handle_unregister_shbuffergroupEP25resfact_register_sb_msg_tj13audit_token_t
- ____ZN17PSResourceFactory28handleResourceFactoryMessageEP17res_factory_msg_tjP21mach_msg_descriptor_ti_block_invoke
CStrings:
+ "%s: Rejected CLIENT_DIED message from unauthorized sender\n"
+ "%s: Rejecting CLIENT_DIED from unauthorized pid=%d (expected polarisd pid=%d)\n"
+ "%s: Rejecting non-zero map_addr from external process (type: %d flags: %x pid: %d map_addr: %lx)\n"
+ "%s: frame_history_server is null, ignoring frame history request from pid=%d\n"
+ "%s: handle_frame_history_info failed\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pIArzG/Sources/ApplePolaris/PolarisBufferService/CameraInterface/PSSharedCameraStream.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pIArzG/Sources/ApplePolaris/PolarisBufferService/CameraInterface/PSSharedCameraStreamWriterImpl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.pIArzG/Sources/ApplePolaris/PolarisBufferService/CameraInterface/PSSharedCameraSuperframeStreamWriter.cpp"
+ "23:35:43"
+ "Jun 26 2026"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.l4IbuX/Sources/ApplePolaris/PolarisBufferService/CameraInterface/PSSharedCameraStream.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.l4IbuX/Sources/ApplePolaris/PolarisBufferService/CameraInterface/PSSharedCameraStreamWriterImpl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.l4IbuX/Sources/ApplePolaris/PolarisBufferService/CameraInterface/PSSharedCameraSuperframeStreamWriter.cpp"
- "21:49:54"
- "Jun 16 2026"

```
