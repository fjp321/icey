sudo pkill mpd
sudo systemctl restart icecast2
# download_all_playlist.sh
mpd ~/.config/mpd/angery.conf
mpd ~/.config/mpd/blue.conf
mpd ~/.config/mpd/peachy.conf
mpd ~/.config/mpd/fast.conf

ports=('6599' '6598' '6597' '6596')
for port in ${ports[@]};
do
	echo -e "Updating for port ${port}"
        mpc --host="${MPD_PASS}@localhost" --port=${port} update
	mpc --host="${MPD_PASS}@localhost" --port=${port} add /
	mpc --host="${MPD_PASS}@localhost" --port=${port} random on
	mpc --host="${MPD_PASS}@localhost" --port=${port} volume 70
	mpc --host="${MPD_PASS}@localhost" --port=${port} play
done
