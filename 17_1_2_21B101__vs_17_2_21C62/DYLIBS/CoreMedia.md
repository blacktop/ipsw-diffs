## CoreMedia

> `/System/Library/Frameworks/CoreMedia.framework/CoreMedia`

```diff

-3085.13.4.1.5
-  __TEXT.__text: 0x139b98
+3090.15.1.6.0
+  __TEXT.__text: 0x13aa00
   __TEXT.__auth_stubs: 0x2fe0
   __TEXT.__objc_methlist: 0x2c
   __TEXT.__const: 0x1618
-  __TEXT.__cstring: 0x185e4
-  __TEXT.__oslogstring: 0x3773
+  __TEXT.__cstring: 0x18856
+  __TEXT.__oslogstring: 0x39eb
   __TEXT.__gcc_except_tab: 0xdc
   __TEXT.__dlopen_cstrs: 0x143
-  __TEXT.__unwind_info: 0x39bc
+  __TEXT.__unwind_info: 0x39d4
   __TEXT.__objc_classname: 0x3b
   __TEXT.__objc_methname: 0x5ed
   __TEXT.__objc_methtype: 0xc0
   __TEXT.__objc_stubs: 0x840
   __DATA_CONST.__got: 0x418
-  __DATA_CONST.__const: 0x8648
+  __DATA_CONST.__const: 0x86d0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x110
   __DATA_CONST.__objc_selrefs: 0x220
-  __AUTH_CONST.__const: 0x4120
-  __AUTH_CONST.__cfstring: 0x138a0
+  __AUTH_CONST.__const: 0x4180
+  __AUTH_CONST.__cfstring: 0x13980
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_const: 0x48
   __AUTH_CONST.__auth_got: 0x1800

   __DATA.__objc_classrefs: 0x78
   __DATA.__objc_superrefs: 0x8
   __DATA.__objc_ivar: 0x4
-  __DATA.__data: 0xe39
+  __DATA.__data: 0xe41
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x29f8
+  __DATA.__bss: 0x2a38
   __DATA.__common: 0x1c0
   __DATA_DIRTY.__data: 0x274
   __DATA_DIRTY.__common: 0xa8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 61376BCD-9D46-35A2-A377-379569CEDB2D
-  Functions: 5078
-  Symbols:   12198
-  CStrings:  6850
+  UUID: 196713DD-884E-34DE-8761-8D84A646F868
+  Functions: 5083
+  Symbols:   12228
+  CStrings:  6880
 
Symbols:
+ _FigBufferedAirPlayClientRoutingRegistryCreate.onceToken
+ _SANDBOX_EXTENSION_DEFAULT
+ ___FigBufferedAirPlayClientRoutingRegistryCreate_block_invoke
+ ___FigSandboxRegistrationServerStart_block_invoke.8
+ ___block_literal_global.12
+ ___block_literal_global.22
+ ___figSandboxRegistrationRecordForDiagnosticLogging_block_invoke
+ ___figSandboxRegistrationRecordForDiagnosticLogging_block_invoke_2
+ _figSandboxRegistrationDumpAllApply
+ _figSandboxRegistrationRecordForDiagnosticLogging.mutex
+ _figSandboxRegistrationRecordForDiagnosticLogging.onceToken
+ _figSandboxRegistrationRecordForDiagnosticLogging.sandboxRegistrations
+ _kCMFormatDescriptionLogTransferFunction_AppleLog
+ _kFigAirPlayCustomURLResponseKey_ContentRenewalTimeDiff
+ _kFigEndpointStreamNotification_AudioCapabilitiesChanged
+ _kFigEndpointStreamProperty_SupportedAudioCapabilities
+ _kFigEndpointStreamSupportedAudioCapabilities_SupportedChannelLayoutTags
+ _kFigSandboxRegistrationXPCMsgParam_SandboxExtensionPath
+ _mediaexperience
+ _routingRegistry_figRoutingContextCopyProperty
+ _sFigRoutingContextCopySystemAudioContext
+ _sFigRoutingContextCopySystemMusicContext
+ _skFigRoutingContextProperty_ContextUUID
- _SANDBOX_EXTENSION_CANONICAL
- ___FigSandboxRegistrationServerStart_block_invoke.7
CStrings:
+ "/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience"
+ "<< FigXPC >> %s: Error during server setup %d"
+ "<<<< FigBufferedAirPlayClientRoutingRegistry >>>> %s: Did not find MediaExperience bundle '%{public}s': %{public}s\n"
+ "<<<< FigBufferedAirPlayClientRoutingRegistry >>>> %s: FigRoutingContextCopySystemAudioContext is NULL"
+ "<<<< FigBufferedAirPlayClientRoutingRegistry >>>> %s: FigRoutingContextCopySystemMusicContext is NULL"
+ "<<<< FigBufferedAirPlayClientRoutingRegistry >>>> %s: Using System Music RoutingContextUUID [%@] for non-groupable endpoint activated with RoutingContextUUID [%@]\n"
+ "<<<< SandboxRegistration >>>> %s: PID %{public}5@ %{public}-18@ ---- %ld registration%{public}s -----"
+ "<FigSandboxRegistration %p> for client PID %d - %@"
+ "<FigSandboxRegistration %p> hold <extensionHandle %lld> for client PID %d - %@"
+ "<REDACTED>"
+ "AudioCapabilitiesChanged"
+ "CMMutableTagCollection"
+ "ExtensionPath"
+ "FCUP_Response_ContentRenewalTimeDiff"
+ "FigRoutingContextCopySystemAudioContext"
+ "FigRoutingContextCopySystemMusicContext"
+ "LoadMediaExperienceFramework"
+ "Sandbox Registrations"
+ "SupportedAudioCapabilities"
+ "SupportedAudioCapabilities_SupportedChannelLayoutTags"
+ "com.apple.rec2020.apple-log"
+ "figSandboxRegistrationDumpAll"
+ "figXPCConnection_handleServerLaunchOrRelaunch"
+ "kFigRoutingContextProperty_ContextUUID"
+ "routingRegistry_figRoutingContextCopySystemAudioContext"
+ "routingRegistry_figRoutingContextCopySystemMusicContext"
+ "s"
- "<FigSandboxRegistration %p> for client PID %d"
- "<FigSandboxRegistration %p> hold <extensionHandle %lld> for client PID %d"
- "CFMutableTagCollection"
- "CFTagCollection"

```
