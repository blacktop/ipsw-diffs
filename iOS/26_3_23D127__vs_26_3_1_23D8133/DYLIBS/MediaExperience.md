## MediaExperience

> `/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience`

```diff

 315.6.1.0.0
-  __TEXT.__text: 0x201828
+  __TEXT.__text: 0x203984
   __TEXT.__auth_stubs: 0x1fe0
   __TEXT.__delay_helper: 0x1b8
-  __TEXT.__objc_methlist: 0x5f0c
-  __TEXT.__cstring: 0x2efb9
-  __TEXT.__const: 0x1ba8
+  __TEXT.__objc_methlist: 0x601c
+  __TEXT.__cstring: 0x2f32e
+  __TEXT.__const: 0x1bc8
   __TEXT.__gcc_except_tab: 0x3040
-  __TEXT.__oslogstring: 0x3d52a
+  __TEXT.__oslogstring: 0x3dcf0
   __TEXT.__dlopen_cstrs: 0x5bd
-  __TEXT.__unwind_info: 0x4a88
-  __TEXT.__objc_classname: 0x75e
-  __TEXT.__objc_methname: 0x15df0
+  __TEXT.__unwind_info: 0x4ac8
+  __TEXT.__objc_classname: 0x78c
+  __TEXT.__objc_methname: 0x160df
   __TEXT.__objc_methtype: 0x215f
-  __TEXT.__objc_stubs: 0xd660
+  __TEXT.__objc_stubs: 0xd8a0
   __DATA_CONST.__got: 0xaa8
   __DATA_CONST.__const: 0x6618
-  __DATA_CONST.__objc_classlist: 0x1f0
+  __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3be8
-  __DATA_CONST.__objc_superrefs: 0x1d8
+  __DATA_CONST.__objc_selrefs: 0x3c78
+  __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x70
   __AUTH_CONST.__auth_got: 0x1008
   __AUTH_CONST.__const: 0x3ea0
-  __AUTH_CONST.__cfstring: 0x18e20
-  __AUTH_CONST.__objc_const: 0x8ba0
+  __AUTH_CONST.__cfstring: 0x18f80
+  __AUTH_CONST.__objc_const: 0x8d68
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0xa00
+  __AUTH.__objc_data: 0xa50
   __AUTH.__data: 0x570
-  __DATA.__objc_ivar: 0x878
+  __DATA.__objc_ivar: 0x88c
   __DATA.__data: 0xfe8
-  __DATA.__bss: 0x1849
+  __DATA.__bss: 0x1859
   __DATA.__common: 0x4a8
   __DATA_DIRTY.__objc_data: 0x960
   __DATA_DIRTY.__bss: 0x4d0

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AA5B312F-5AC1-33B1-B3B6-38A9B89FF185
-  Functions: 7133
-  Symbols:   22305
-  CStrings:  14571
+  UUID: 08B6DD46-6971-39B3-B096-EA519FCC83E4
+  Functions: 7158
+  Symbols:   22388
+  CStrings:  14652
 
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
+ GCC_except_table78
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
+ ___MXCoreSessionSetProperty_block_invoke.174
+ ___MXCoreSessionSetProperty_block_invoke.177
+ ___MXCoreSessionSetProperty_block_invoke.183
+ ___MXCoreSessionSetProperty_block_invoke.191
+ ___block_literal_global.170
+ ___block_literal_global.173
+ ___block_literal_global.176
+ ___block_literal_global.185
+ ___block_literal_global.199
+ ___block_literal_global.250
+ ___block_literal_global.307
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
- GCC_except_table77
- __OBJC_$_CLASS_METHODS_MXSessionManagerBase
- ___MXCoreSessionSetProperty_block_invoke.173
- ___MXCoreSessionSetProperty_block_invoke.176
- ___MXCoreSessionSetProperty_block_invoke.182
- ___MXCoreSessionSetProperty_block_invoke.190
- ___block_literal_global.167
- ___block_literal_global.169
- ___block_literal_global.172
- ___block_literal_global.198
- ___block_literal_global.249
- ___block_literal_global.30
- ___block_literal_global.306
- ___block_literal_global.36
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
+ "23:41:24"
+ "ExternalSecureInput"
+ "ExternalSecureInputPort={PortID:%u, name='%@', accessCount=%d, isMuted:%@}"
+ "Jan 20 2026"
+ "MXExternalSecureInputPort"
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
- "00:21:35"
- "Jan 21 2026"

```
