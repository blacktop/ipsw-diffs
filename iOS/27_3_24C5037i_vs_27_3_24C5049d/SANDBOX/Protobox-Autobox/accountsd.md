## accountsd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.certui.relay"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc"))
+		(require-not (global-name "com.apple.identityservicesd.idquery.embedded.auth"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.icloud.searchpartyd.beaconmanager"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))

 (deny system-necp-client-action)
 (allow system-necp-client-action
 	(necp-client-action
+		28
 		NECP_CLIENT_ACTION_ACQUIRE_AGENT_TOKEN
 		NECP_CLIENT_ACTION_ADD
 		NECP_CLIENT_ACTION_ADD_FLOW
```
