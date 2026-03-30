## bluetoothd

> `/usr/sbin/bluetoothd`

```diff

-194.26.2.0.0
-  __TEXT.__text: 0x8608a4
+195.4.1.1.0
+  __TEXT.__text: 0x8614d4
   __TEXT.__auth_stubs: 0x4ce0
-  __TEXT.__objc_stubs: 0x170c0
-  __TEXT.__init_offsets: 0x64
-  __TEXT.__objc_methlist: 0x8784
+  __TEXT.__objc_stubs: 0x17120
+  __TEXT.__init_offsets: 0x60
+  __TEXT.__objc_methlist: 0x8794
   __TEXT.__const: 0x2517c
-  __TEXT.__gcc_except_tab: 0x6c15c
-  __TEXT.__cstring: 0xb3748
+  __TEXT.__gcc_except_tab: 0x6c108
+  __TEXT.__cstring: 0xb407f
   __TEXT.__objc_classname: 0x9aa
-  __TEXT.__objc_methname: 0x1bb41
+  __TEXT.__objc_methname: 0x1bbe4
   __TEXT.__objc_methtype: 0x47bd
-  __TEXT.__oslogstring: 0xae6ff
+  __TEXT.__oslogstring: 0xae597
   __TEXT.__swift5_typeref: 0x9c
   __TEXT.__swift5_capture: 0x68
   __TEXT.__constg_swiftt: 0x48

   __TEXT.__swift_as_ret: 0x8
   __TEXT.__ustring: 0x34
   __TEXT.__dlopen_cstrs: 0xd4
-  __TEXT.__unwind_info: 0x230f0
+  __TEXT.__unwind_info: 0x230d0
   __TEXT.__eh_frame: 0x1b0
   __DATA_CONST.__auth_got: 0x2688
-  __DATA_CONST.__got: 0xe30
+  __DATA_CONST.__got: 0xe28
   __DATA_CONST.__auth_ptr: 0x228
-  __DATA_CONST.__const: 0x30670
-  __DATA_CONST.__cfstring: 0x23840
+  __DATA_CONST.__const: 0x30668
+  __DATA_CONST.__cfstring: 0x23900
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xb8

   __DATA_CONST.__objc_dictobj: 0x2f8
   __DATA_CONST.__objc_arrayobj: 0x1f8
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0xead0
-  __DATA.__objc_selrefs: 0x6a58
-  __DATA.__objc_ivar: 0xfd8
+  __DATA.__objc_const: 0xeb20
+  __DATA.__objc_selrefs: 0x6a68
+  __DATA.__objc_ivar: 0xfe0
   __DATA.__objc_data: 0x1a58
-  __DATA.__data: 0x4928
+  __DATA.__data: 0x48e8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x72952
+  __DATA.__bss: 0x72932
   __DATA.__common: 0x6f80
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 58F4BA7F-2E62-3E04-8ABB-03D06FD7A591
-  Functions: 34235
+  UUID: 96E72DE8-A670-3264-818F-CD17B0C7BC13
+  Functions: 34230
   Symbols:   1721
-  CStrings:  43904
+  CStrings:  43950
 
CStrings:
+ "%s status Connection is invalid. Handle:%X"
+ "%s: connection handle %p is invalid (already freed?), cleaning up TS peer entries"
+ "/private/var/Managed Preferences/mobile/com.apple.bluetooth.plist"
+ "1cb11066a2b836617cdaf6ad78336b1f4325de92e90a2ff3e588ca9409bf73fa"
+ "21:05:32"
+ "9d53d02b1e9bd5bf44a6384bb75baad830bbbc458a93743e478a608042981864"
+ "BTMAPDisabled"
+ "BT_TS_BTDisconnected"
+ "BT_TS_MoveL2CAPChannels: currentHandle=%p is invalid (already freed?), best-effort drain to newHandle=%p"
+ "BT_TS_MoveL2CAPChannels: invalid newHandle=%p"
+ "CBExtension: ignore proximityServiceData mismatch: %@ vs %@"
+ "Denying connection attempt from device %{public}s"
+ "FilterProximityServiceData: <%@> -> <%@>"
+ "Invalid Connection Handle in for transportTech:%d reason:%d"
+ "Invalid size in ENHANCED LE Connection Oriented L2CAP Channel Connection Request : %d (minimum %d)"
+ "Invalid size in ENHANCED LE Connection Oriented L2CAP Channel Connection Response : %d (minimum %d)"
+ "Invalid size in ENHANCED LE Connection Oriented L2CAP Channel Reconfig Request : %d (minimum %d)"
+ "Invalid size in command rejected : %d (minimum %d)"
+ "L2CAPAGG RX: Connection freed during packet processing, stopping."
+ "Mar 25 2026"
+ "OI_DevMgr_PolicyACLDisconnected"
+ "OI_HCIEventHandler_DisconnectionComplete invalid connection handle, ignoring"
+ "OI_LP_DisconnectInd"
+ "Prox pairing profile is installed"
+ "Rejecting MAP connection due to device tag"
+ "Remote alert start: processIdentity=%@, bundleID=%@, scene=%@"
+ "Remote transport error but alternate handle %p is %s for Peer %d, pipeID=0x%4x"
+ "Sending DOWNGRADE: invalid connection handle %p"
+ "Sending DOWNGRADE_CFM: invalid connection handle %p"
+ "Sending DOWNGRADE_REQ: invalid connection handle %p"
+ "Sending UPGRADE: invalid connection handle %p"
+ "Sending UPGRADE_CFM: invalid connection handle %p"
+ "Sending UPGRADE_COMPLETE: invalid connection handle %p"
+ "Sending UPGRADE_COMPLETE_CFM: invalid connection handle %p"
+ "T@\"NSData\",R,C,N,V_prefFilterProximityServiceData"
+ "TS_DataCb: stale connection handle %p for pipeID 0x%4x"
+ "_prefFilterProximityServiceData"
+ "_proxPairingProfileInstalled"
+ "cba8d1f838740555b0c3f8eb5fb44576213b568bc9e8fb5cc37be75d156800fe"
+ "channel already freed"
+ "commonTransportConnectionComplete: SendUpgradeComplete failed after policy failure, resetting state"
+ "commonTransportConnectionComplete: SendUpgradeComplete failed, resetting state"
+ "enableAccessorySetupTesting"
+ "filterProximityServiceData"
+ "postConnectCompleteDisconnected"
+ "prefFilterProximityServiceData"
+ "proximityServiceData"
+ "receivedUpgradeCfm: SendUpgradeComplete failed, resetting state for peer %d"
+ "receivedUpgradeCompleteCfm: unstallL2CAPForHandle failed for handle %p, continuing cleanup"
+ "stallL2CAPForHandle: invalid connection handle %p"
+ "unstallL2CAPForHandle: invalid connection handle %p"
- "$$$ Remote alert start: processIdentity=%@, bundleID=%@, scene=%@"
- "20:24:24"
- "Denying connection attempt from device %{public}s. Is MAP enabled? Is MAP connected to some other device?"
- "HeySiriScanProt: Blocking fScanFiltersNeedUpdating in scan() from \"%s\""
- "HeySiriScanProt: Blocking shouldUpdateState in stopScan() from \"%s\""
- "HeySiriScanProt: Bypassing tryUpdateScanState"
- "HeySiriScanProt: Deactivating (external scan agent)"
- "HeySiriScanProt: Protecting. needToRestart=%u"
- "HeySiriScanProt: Starting (%llu nsec)"
- "HeySiriScanProt: Stopping"
- "Mar  9 2026"

```
