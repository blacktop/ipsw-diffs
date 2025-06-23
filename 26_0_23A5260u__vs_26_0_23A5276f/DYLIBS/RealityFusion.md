## RealityFusion

> `/System/Library/PrivateFrameworks/RealityFusion.framework/RealityFusion`

```diff

-403.0.9.502.4
-  __TEXT.__text: 0x8ef88
+403.0.15.0.5
+  __TEXT.__text: 0x8ef7c
   __TEXT.__auth_stubs: 0x1d60
   __TEXT.__objc_methlist: 0x34c
   __TEXT.__const: 0x952a
   __TEXT.__gcc_except_tab: 0x86a8
   __TEXT.__cstring: 0x32e7
-  __TEXT.__oslogstring: 0x22fe
+  __TEXT.__oslogstring: 0x236e
   __TEXT.__ustring: 0x72
   __TEXT.__unwind_info: 0x3050
   __TEXT.__eh_frame: 0x58

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1709053F-3153-3C26-83D2-0FC618385713
+  UUID: 389ACAA0-B4D0-31F0-BAAC-955812E2F402
   Functions: 2619
   Symbols:   7391
   CStrings:  833
Functions:
~ __ZN2rf6detail16removeMeshesFromERNS_17LockedARStateDataEONSt3__16vectorINS_9data_flow6RFUUIDENS3_9allocatorIS6_EEEEb : 804 -> 792
CStrings:
+ "ARState: Got an operation with a pinned group or pinned anchor that wasn't in the state. The pinned group is %{public}s and the pinned anchor is %{public}s"
+ "ARState: Inserting anchor %{public}s to pinned group %{public}s"
+ "ARState: Loaded new pinned group %{public}s"
+ "ARState: Removing anchor %{public}s from pinned group %{public}s"
+ "ARState: Removing mesh %{public}s"
+ "ARState: switch current room to %{public}s"
+ "AnchorListenerConsumer: calling pinned group change callback on anchor %{public}s with group %{public}s"
+ "DebugOptionConsumer: Room client referencing anchor %{public}s while it's not in the anchor dictionary."
+ "RFARSessionObserver: Attempting to re-add anchor %{public}s in queue to ARKit"
+ "RFPinnedGroupPtrVisitAnchors: Anchor %{public}s is nullptr in pinned group %{public}s, RF internal state could potentially be corrupted."
- "ARState: Got an operation with a pinned group or pinned anchor that wasn't in the state. The pinned group is %s and the pinned anchor is %s"
- "ARState: Inserting anchor %s to pinned group %s"
- "ARState: Loaded new pinned group %s"
- "ARState: Removing anchor %s from pinned group %s"
- "ARState: Removing mesh %s{public}"
- "ARState: switch current room to %s"
- "AnchorListenerConsumer: calling pinned group change callback on anchor %s with group %s"
- "DebugOptionConsumer: Room client referencing anchor %s while it's not in the anchor dictionary."
- "RFARSessionObserver: Attempting to re-add anchor %s in queue to ARKit"
- "RFPinnedGroupPtrVisitAnchors: Anchor %s is mullptr in pinned group %s, RF internal state could potentially be corrupted."

```
