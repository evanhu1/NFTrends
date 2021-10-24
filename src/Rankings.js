import React, { Component, useEffect } from 'react';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import { tableCellClasses } from "@mui/material/TableCell";
import { Container } from '@mui/material';
import Typography from '@mui/material/Typography';


import './Rankings.css';
const columns = [
    { id: 'rank', label: 'Rank', minWidth: 1/3 },
    { id: 'name', label: 'Name', minWidth: 1/3 },
    { id: 'tweets', label: 'Tweets', align: 'right', format: (value) => value.toLocaleString('en-US') }
  ];

  function createRankings(data, collections) {
    let rows = [];
    let c = 0;
    data.forEach(nft_collection => {
      rows.push({"rank" : c + 1, "name" : collections[c]["collection_name"], "tweets" : data["count"], "imgUrl": collections[c]["image_url"], "desc": collections[c]["description"]});
      c += 1;
    });
    return rows
  }

  export default function Rankings ({setSelectedID}) {
    const onButtonClick=(id)=>{
      console.log(id)
      setSelectedID(id)
    }
  const [rows, setRows] = React.useState([]);
  var collections;
  fetch('/api/nft_collections')
      .then(res => res.json())
      .then(data => {collections = data;});
  useEffect(() => {
    fetch('/api/data')
      .then(res => res.json())
      .then(data => {});
    fetch('/api/analytic')
      .then(res => res.json())
      .then(data => {setRows(createRankings(data, collections));});
  });
  
  return(
    <Container style={{marginTop: '10%'}}>
      <Paper sx={{ width: '100%', overflow: 'hidden' }}>
        <Typography sx={{fontSize: '3rem', marginLeft: '5%'}} color="white" align="left">Trending NFTs</Typography>
          <TableContainer sx={{ maxHeight: 7/10, width: '90%', margin: '5%' }}>
            <Table stickyHeader aria-label="sticky table" sx={{
              [`& .${tableCellClasses.root}`]: {
                borderBottom: "none"
              }
            }}>
            <TableHead>
              <TableRow>
                {columns.map((column) => ( 
                  <TableCell
                    key={column.id}
                    align={column.align}
                    style={{ minWidth: 1/5, color: 'white'}}>
                    {column.label}
                  </TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
                {rows.map((row) => {
                  return (
                    <TableRow hover role="checkbox" tabIndex={-1} key={row.code} sx = {{height: 60}}>
                      {columns.map((column) => {
                        const value = row[column.id];
                        return (
                          <TableCell onClick={()=>onButtonClick(row)} key={column.id} align={column.align} style={{fontSize: 20, color: 'white'}}>
                            {column.format && typeof value === 'number'
                              ? column.format(value)
                              : value}
                          </TableCell>
                        );
                      })}
                    </TableRow>
                  );
                })}
            </TableBody>
          </Table>
        </TableContainer>
      </Paper>
    </Container>
  );
      
    
}