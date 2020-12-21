from pydrive.auth import GoogleAuth

def auth():
	gauth = GoogleAuth()
	gauth.LoadCredentialsFile("credencial.txt")
	if gauth.credentials is None:
	    gauth.LocalWebserverAuth()
	elif gauth.access_token_expired:
	    gauth.Refresh()
	else:
	    gauth.Authorize()
	gauth.SaveCredentialsFile("credencial.txt")

	return gauth

