## IOUIAngel

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (global-name "com.apple.uikit.viewservice.com.apple.InCallService"))
+		(require-not (global-name "com.apple.assistant.dictation"))
 		(require-not (global-name "com.apple.PointerUI.pointeruid.service"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.PowerManagement.control"))

 
 (deny system-necp-client-action)
 (allow system-necp-client-action
-	(necp-client-action NECP_CLIENT_ACTION_ADD)
+	(necp-client-action
+		NECP_CLIENT_ACTION_ADD
+		NECP_CLIENT_ACTION_COPY_RESULT
+		NECP_CLIENT_ACTION_REMOVE)
 )
 
 (allow process-exec-update-label)
```
