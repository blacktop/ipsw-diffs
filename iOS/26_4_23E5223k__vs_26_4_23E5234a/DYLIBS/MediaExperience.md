## MediaExperience

> `/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience`

```diff

 320.22.1.0.0
-  __TEXT.__text: 0x203e9c
+  __TEXT.__text: 0x205fd8
   __TEXT.__auth_stubs: 0x1fe0
   __TEXT.__delay_helper: 0x1b8
-  __TEXT.__objc_methlist: 0x6214
-  __TEXT.__cstring: 0x2fdd5
-  __TEXT.__const: 0x1bb8
+  __TEXT.__objc_methlist: 0x6324
+  __TEXT.__cstring: 0x3014a
+  __TEXT.__const: 0x1bd8
   __TEXT.__gcc_except_tab: 0x30dc
-  __TEXT.__oslogstring: 0x3ec5a
+  __TEXT.__oslogstring: 0x3f420
   __TEXT.__dlopen_cstrs: 0x5bd
-  __TEXT.__unwind_info: 0x4d08
-  __TEXT.__objc_classname: 0x7b6
-  __TEXT.__objc_methname: 0x16748
+  __TEXT.__unwind_info: 0x4d50
+  __TEXT.__objc_classname: 0x7e4
+  __TEXT.__objc_methname: 0x16a37
   __TEXT.__objc_methtype: 0x2225
-  __TEXT.__objc_stubs: 0xdce0
+  __TEXT.__objc_stubs: 0xdf20
   __DATA_CONST.__got: 0xab8
   __DATA_CONST.__const: 0x6668
-  __DATA_CONST.__objc_classlist: 0x208
+  __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d90
-  __DATA_CONST.__objc_superrefs: 0x1f0
+  __DATA_CONST.__objc_selrefs: 0x3e20
+  __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_arraydata: 0x70
   __AUTH_CONST.__auth_got: 0x1008
   __AUTH_CONST.__const: 0x3fe8
-  __AUTH_CONST.__cfstring: 0x191a0
-  __AUTH_CONST.__objc_const: 0x90d8
+  __AUTH_CONST.__cfstring: 0x19300
+  __AUTH_CONST.__objc_const: 0x92a0
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0xaf0
+  __AUTH.__objc_data: 0xb40
   __AUTH.__data: 0x570
-  __DATA.__objc_ivar: 0x8d0
+  __DATA.__objc_ivar: 0x8e4
   __DATA.__data: 0x1000
-  __DATA.__bss: 0x1898
+  __DATA.__bss: 0x18a8
   __DATA.__common: 0x4a8
   __DATA_DIRTY.__objc_data: 0x960
   __DATA_DIRTY.__bss: 0x4e0

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C1FDB04B-1944-35D0-BDF5-CD63B981701B
-  Functions: 7448
-  Symbols:   23169
-  CStrings:  14835
+  UUID: 31A10980-0BB3-37C8-9FAA-9D49CEB8654B
+  Functions: 7473
+  Symbols:   23252
+  CStrings:  14916
 
Symbols:
+ +[MXSessionManagerBase externalSecureInputPortsLock]
+ +[MXSessionManagerBase externalSecureInputPorts]
+ +[MXSessionManagerBase(ExternalSecureInput) dumpExternalSecureInputDebugInfo]
+ +[MXSessionManagerBase(ExternalSecureInput) handleExternalSecureInputPortConnected:]
+ +[MXSessionManagerBase(ExternalSecureInput) handleExternalSecureInputPortDisconnected:]
+ +[MXSessionManagerBase(ExternalSecureInput) updateExternalSecureInputPortMuteState:reason:]
+ +[MXSessionManagerBase(ExternalSecureInput) updateExternalSecureInputPortMuteState:reason:].cold.1
+ +[MXSessionManagerBase(ExternalSecureInput) updateExternalSecureInputPortsCache:]
+ -[MXCoreSessionBase activeExternalSecureRecordingPortID]
+ -[MXCoreSessionBase lastExternalSecureRecordingPortID]
+ -[MXCoreSessionBase setLastExternalSecureRecordingPortID:]
+ -[MXExternalSecureInputPort accessCount]
+ -[MXExternalSecureInputPort dealloc]
+ -[MXExternalSecureInputPort description]
+ -[MXExternalSecureInputPort init:]
+ -[MXExternalSecureInputPort isMuted]
+ -[MXExternalSecureInputPort name]
+ -[MXExternalSecureInputPort portID]
+ -[MXExternalSecureInputPort setAccessCount:]
+ -[MXExternalSecureInputPort setIsMuted:]
+ -[MXExternalSecureInputPort updateAccessCount:reason:increment:]
+ -[MXExternalSecureInputPort updateMuteStateIfNeeded]
+ -[MXSessionManager(Utilities) updateExternalSecureInputPortsMuteStateIfNeeded]
+ GCC_except_table84
+ _OBJC_CLASS_$_MXExternalSecureInputPort
+ _OBJC_IVAR_$_MXCoreSessionBase._lastExternalSecureRecordingPortID
+ _OBJC_IVAR_$_MXExternalSecureInputPort._accessCount
+ _OBJC_IVAR_$_MXExternalSecureInputPort._isMuted
+ _OBJC_IVAR_$_MXExternalSecureInputPort._name
+ _OBJC_IVAR_$_MXExternalSecureInputPort._portID
+ _OBJC_METACLASS_$_MXExternalSecureInputPort
+ __OBJC_$_CLASS_METHODS_MXSessionManagerBase(ExternalSecureInput)
+ __OBJC_$_CLASS_PROP_LIST_MXSessionManagerBase
+ __OBJC_$_INSTANCE_METHODS_MXExternalSecureInputPort
+ __OBJC_$_INSTANCE_VARIABLES_MXExternalSecureInputPort
+ __OBJC_$_PROP_LIST_MXExternalSecureInputPort
+ __OBJC_CLASS_RO_$_MXExternalSecureInputPort
+ __OBJC_METACLASS_RO_$_MXExternalSecureInputPort
+ ___MXCoreSessionSetProperty_block_invoke.175
+ ___MXCoreSessionSetProperty_block_invoke.178
+ ___MXCoreSessionSetProperty_block_invoke.181
+ ___MXCoreSessionSetProperty_block_invoke.189
+ ___block_literal_global.169
+ ___block_literal_global.171
+ ___block_literal_global.183
+ ___block_literal_global.197
+ ___block_literal_global.248
+ ___block_literal_global.305
+ ___block_literal_global.33
+ ___block_literal_global.53
+ ___cmsSetIsActive_block_invoke.148
+ ___cmsmInitializeCMSessionManager_block_invoke.35
+ ___cmsmInitializeCMSessionManager_block_invoke_2.41
+ _objc_msgSend$accessCount
+ _objc_msgSend$activeExternalSecureRecordingPortID
+ _objc_msgSend$dumpExternalSecureInputDebugInfo
+ _objc_msgSend$externalSecureInputPorts
+ _objc_msgSend$externalSecureInputPortsLock
+ _objc_msgSend$handleExternalSecureInputPortConnected:
+ _objc_msgSend$handleExternalSecureInputPortDisconnected:
+ _objc_msgSend$init:
+ _objc_msgSend$isMuted
+ _objc_msgSend$lastExternalSecureRecordingPortID
+ _objc_msgSend$portID
+ _objc_msgSend$setAccessCount:
+ _objc_msgSend$setLastExternalSecureRecordingPortID:
+ _objc_msgSend$updateAccessCount:reason:increment:
+ _objc_msgSend$updateExternalSecureInputPortMuteState:reason:
+ _objc_msgSend$updateExternalSecureInputPortsCache:
+ _objc_msgSend$updateExternalSecureInputPortsMuteStateIfNeeded
+ _objc_msgSend$updateMuteStateIfNeeded
+ _sExternalSecureInputPorts
+ _sExternalSecureInputPortsLock
+ _vaeDoesPortSupportExternalSecureMute
+ _vaeSetExternalSecureMute
- GCC_except_table83
- __OBJC_$_CLASS_METHODS_MXSessionManagerBase
- ___MXCoreSessionSetProperty_block_invoke.174
- ___MXCoreSessionSetProperty_block_invoke.177
- ___MXCoreSessionSetProperty_block_invoke.180
- ___MXCoreSessionSetProperty_block_invoke.188
- ___block_literal_global.170
- ___block_literal_global.173
- ___block_literal_global.176
- ___block_literal_global.179
- ___block_literal_global.182
- ___block_literal_global.247
- ___block_literal_global.30
- ___block_literal_global.304
- ___block_literal_global.32
- ___block_literal_global.42
- ___cmsSetIsActive_block_invoke.147
- ___cmsmInitializeCMSessionManager_block_invoke.34
- ___cmsmInitializeCMSessionManager_block_invoke_2.40
CStrings:
+ "+[MXSessionManagerBase(ExternalSecureInput) dumpExternalSecureInputDebugInfo]"
+ "+[MXSessionManagerBase(ExternalSecureInput) handleExternalSecureInputPortConnected:]"
+ "+[MXSessionManagerBase(ExternalSecureInput) handleExternalSecureInputPortDisconnected:]"
+ "+[MXSessionManagerBase(ExternalSecureInput) updateExternalSecureInputPortMuteState:reason:]"
+ "+[MXSessionManagerBase(ExternalSecureInput) updateExternalSecureInputPortsCache:]"
+ "-CMSessionMgr- %s: Failed to update the external secure input port mute state for session '%{public}@'"
+ "-CMVAEndpoint- %s: Failed to set ExternalSecureMute because port(PortID='%u') doesn't support it!"
+ "-CMVAEndpoint- %s: Failed to set ExternalSecureMute property - PortID='%u' err='%c%c%c%c'"
+ "-CMVAEndptMgr- %s: New input port: Name='%{private}@' ConnectionType='%c%c%c%c' UID='%{public}@' PortType='%c%c%c%c' PortID='%u' IsQuiesceableWiredPort='%{BOOL}u' SupportsExternalSecureInputMute='%{BOOL}u'"
+ "-MXSessionManagerBaseExternalSecureInput- %s: ##################################################### External Secure Input Ports ####################################################"
+ "-MXSessionManagerBaseExternalSecureInput- %s: #######################################################################################################################################"
+ "-MXSessionManagerBaseExternalSecureInput- %s: %{public}@ is successfully %{public}@"
+ "-MXSessionManagerBaseExternalSecureInput- %s: %{public}@ is successfully muted since it just got connected"
+ "-MXSessionManagerBaseExternalSecureInput- %s: Adding connected %{public}@"
+ "-MXSessionManagerBaseExternalSecureInput- %s: Detected disconnected port %{public}@ during cache update, reason: %{public}@"
+ "-MXSessionManagerBaseExternalSecureInput- %s: ExternalSecureInputPorts[%ld] %{public}@"
+ "-MXSessionManagerBaseExternalSecureInput- %s: Failed to %{public}@ %{public}@"
+ "-MXSessionManagerBaseExternalSecureInput- %s: No connected input ports found"
+ "-MXSessionManagerBaseExternalSecureInput- %s: No external secure input ports to check during cache update"
+ "-MXSessionManagerBaseExternalSecureInput- %s: Removing disconnected %{public}@"
+ "-MXSessionManagerBaseExternalSecureInput- %s: Session '%{public}@' %{public}@ access count for %{public}@ since '%{public}@'"
+ "-MXSessionManagerBaseExternalSecureInput- %s: Session '%{public}@' failed to %{public}@ access count for %{public}@ since '%{public}@' error=%d"
+ "-MXSessionManagerBaseExternalSecureInput- %s: session cannot be nil!"
+ "-MXSessionManagerUtilities- %s: MXSessionManager INTERRUPTING '%{public}@' because updating secure input mute status failed with error =%d"
+ "-[MXExternalSecureInputPort init:]"
+ "-[MXExternalSecureInputPort updateAccessCount:reason:increment:]"
+ "-[MXExternalSecureInputPort updateMuteStateIfNeeded]"
+ "-[MXSessionManager(Utilities) updateExternalSecureInputPortsMuteStateIfNeeded]"
+ "00:20:11"
+ "ExternalSecureInput"
+ "ExternalSecureInputPort={PortID:%u, name='%@', accessCount=%d, isMuted:%@}"
+ "MXExternalSecureInputPort"
+ "Mar  1 2026"
+ "T@\"NSLock\",R"
+ "T@\"NSMutableDictionary\",R"
+ "T@\"NSString\",R,N,V_name"
+ "TB,N,V_isMuted"
+ "TI,N,V_accessCount"
+ "TI,N,V_lastExternalSecureRecordingPortID"
+ "TI,R,N"
+ "TI,R,N,V_portID"
+ "_accessCount"
+ "_isMuted"
+ "_lastExternalSecureRecordingPortID"
+ "_name"
+ "_portID"
+ "accessCount"
+ "activeExternalSecureRecordingPortID"
+ "activeExternalSecureRecordingPortID="
+ "decrement"
+ "decremented"
+ "dumpExternalSecureInputDebugInfo"
+ "externalSecureInputPorts"
+ "externalSecureInputPortsLock"
+ "handleExternalSecureInputPortConnected:"
+ "handleExternalSecureInputPortDisconnected:"
+ "increment"
+ "incremented"
+ "init:"
+ "isMuted"
+ "lastExternalSecureRecordingPortID"
+ "lastExternalSecureRecordingPortID="
+ "portID"
+ "setAccessCount:"
+ "setLastExternalSecureRecordingPortID:"
+ "updateAccessCount:reason:increment:"
+ "updateExternalSecureInputPortMuteState:reason:"
+ "updateExternalSecureInputPortsCache:"
+ "updateExternalSecureInputPortsMuteStateIfNeeded"
+ "updateMuteStateIfNeeded"
+ "vaeSetExternalSecureMute"
- "-CMVAEndptMgr- %s: New input port: Name='%{private}@' ConnectionType='%c%c%c%c' UID='%{public}@' PortType='%c%c%c%c' PortID='%u' IsQuiesceableWiredPort='%{BOOL}u'"
- "20:49:11"
- "Feb 23 2026"

```
